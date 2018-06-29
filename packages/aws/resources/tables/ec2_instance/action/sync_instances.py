# -*- coding: UTF-8 -*-

# test_special_action.py
# Created by Saverio Porcari
# Copyright (c) 2010 Softwell. All rights reserved.

from gnr.web.batch.btcaction import BaseResourceAction

caption = 'Sync instances'
description='Sync instances with AWS'

class Main(BaseResourceAction):
    batch_prefix = 'sync_ec2_instances'
    batch_title = 'Sync instances'
    batch_cancellable = True
    batch_delay = 0.5


    def do(self):
        """'Sync instances'"""
        existing_instances = self.tblobj.query(forUpdate=True).fetchAsDict(key='instanceid')
        aws_manager = self.page.site.getService('aws_softwell')
        instances = aws_manager.ec2_instances()
        n_instances = len(instances.keys())
        for inst_id, inst in self.btc.thermo_wrapper(instances.items(),  message='Instance', maximum=n_instances):
            local_instance = existing_instances.pop(inst_id, None) or dict()
            inst = dict(inst)
            aws_instance = dict([(k.lower(), v) for k,v in inst.items()])
            if local_instance:
                self.tblobj.update(aws_instance, local_instance)
            else:
                self.tblobj.insert(aws_instance)
        if existing_instances:
            self.tblobj.deleteSelection(where='$instanceid IN :inst_ids', inst_ids=existing_instances.keys())
                
        self.db.commit()


    def result_handler(self):
        return 'Execution completed',None
        
    #def table_script_parameters_pane(self,pane,**kwargs):
    #    #pane = pane.contentPane(height='90px',width='300px')
    #    fb = pane.formbuilder(cols=1, border_spacing='5px', colswidth='auto', fld_width='100%', width='400px')
    #    fb.dateTextBox(value='^.data_fine',lbl='Fino alla data', width='8em',  validate_notnull=True)
        