#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('publicdnsname')
        r.fieldcell('ebsoptimized')
        r.fieldcell('launchtime')
        r.fieldcell('publicipaddress')
        r.fieldcell('privateipaddress')
        r.fieldcell('productcodes')
        r.fieldcell('vpcid')
        r.fieldcell('statetransitionreason')
        r.fieldcell('instanceid')
        r.fieldcell('enasupport')
        r.fieldcell('imageid')
        r.fieldcell('privatednsname')
        r.fieldcell('keyname')
        r.fieldcell('clienttoken')
        r.fieldcell('subnetid')
        r.fieldcell('instancetype')
        r.fieldcell('sourcedestcheck')
        r.fieldcell('hypervisor')
        r.fieldcell('architecture')
        r.fieldcell('rootdevicetype')
        r.fieldcell('rootdevicename')
        r.fieldcell('virtualizationtype')
        r.fieldcell('amilaunchindex')

    def th_order(self):
        return 'publicdnsname'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('monitoring')
        fb.field('publicdnsname' )
        fb.field('statereason' , tag='quickGrid')
        fb.field('state' , tag='quickGrid')
        fb.field('ebsoptimized' )
        fb.field('launchtime' )
        fb.field('publicipaddress' )
        fb.field('privateipaddress' )
        fb.field('productcodes' )
        fb.field('vpcid' )
        fb.field('cpuoptions' , tag='quickGrid')
        fb.field('statetransitionreason' )
        fb.field('instanceid' )
        fb.field('enasupport' )
        fb.field('imageid' )
        fb.field('privatednsname' )
        fb.field('keyname' )
        fb.field('securitygroups' , tag='quickGrid')
        fb.field('clienttoken' )
        fb.field('subnetid' )
        fb.field('instancetype' )
        fb.field('networkinterfaces' , tag='quickGrid')
        fb.field('sourcedestcheck' )
        fb.field('placement' , tag='quickGrid')
        fb.field('hypervisor' )
        fb.field('blockdevicemappings' , tag='quickGrid')
        fb.field('architecture' )
        fb.field('rootdevicetype' )
        fb.field('rootdevicename' )
        fb.field('virtualizationtype' )
        fb.field('tags' , tag='quickGrid')
        fb.field('amilaunchindex' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
