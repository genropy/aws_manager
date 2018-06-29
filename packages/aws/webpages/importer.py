# -*- coding: UTF-8 -*-
from gnr.core.gnrbag import Bag
from gnr.core.gnrdecorator import public_method
import os
import re
from gnr.app.gnrdeploy import PathResolver,ThPackageResourceMaker



class GnrCustomWebPage(object):
    py_requires="""package_editor/model_editor:TableModuleEditor"""

    def windowTitle(self):
        return '!!Import tables from AWS'

    def main(self,root,**kwargs):
        bc = root.borderContainer(datapath='importer')
        fb = bc.contentPane(region='top').formbuilder(cols=2)
        fb.button('Get instances', action='FIRE .getInstances;')
        fb.button('Create table', action='FIRE .createTable')
        fb.dataRpc('.instances', self.getInstancesData, _fired='^.getInstances')
        fb.dataRpc('.create_table_out', self.createTable, _fired='^.createTable')

        
        center_pane = bc.contentPane(region='center', datapath='.data')
        center_pane.quickGrid(value='^.instances', height='90%')

        
    @public_method
    def getInstancesData(self):
        aws_manager = self.site.getService('aws_softwell')
        return aws_manager.ec2_instances()


    def getPackagePath(self,project,package):
        path_resolver = PathResolver()
        project_path = path_resolver.project_name_to_path(project)
        return os.path.join(project_path,'packages',package)

    def createModelColumns(self, aws_instance_bag=None):
        result = Bag()
        for name,col_value in aws_instance_bag:
            colname = name.lower().replace(' ','')
            dtype=self.catalog.getClassKey(col_value)
            if dtype =='BAG':
                dtype='X'
            elif dtype == 'NN':
                dtype = 'T'
            name_long = re.sub("([a-z])([A-Z])","\g<1> \g<2>",name)
            b = Bag(dict(name=colname,aws_name=name,
                        name_long=name_long, dtype=dtype))
            result.setItem(colname,b)
        return result

    @public_method
    def createTable(self):
        aws_manager = self.site.getService('aws_softwell')
        instances = aws_manager.ec2_instances()
        tblname='ec2_instance'
        filepath = os.path.join(os.path.join(self.getPackagePath('aws_manager','aws'),'model','%s.py' %tblname))
        table_data = Bag()
        table_data['name'] = tblname
        table_data['_columns'] = self.createModelColumns(aws_instance_bag=instances['#0'].items())
        table_data['pkey']='id'
        table_data['_sysFields']=Bag(dict(id=True, ins=True, upd=True, _enabled=True))
        self.makeOneTable(filepath,table_data=table_data)
        resourceMaker = ThPackageResourceMaker(self.site.gnrapp,package='aws',tables=[tblname], force=True, bag_columns=dict(view=False, form='quickGrid'))
        resourceMaker.makeMenu()
        resourceMaker.makeResources()

    