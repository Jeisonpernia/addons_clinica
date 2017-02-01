# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#    
#    Modulo Desarrollado por Juventud Productiva (Victor Davila)
#    Visitanos en http://juventudproductivabicentenaria.blogspot.com/
#    Nuestro Correo juventudproductivabicentenaria@gmail.com
#
#############################################################################

import openerp
from openerp import tools, api
from openerp.osv import osv, fields
from openerp.http import request

class cli_procedencia_paciente(osv.osv):
    _name = 'cli.procedencia_paciente'
    _rec_name = "partner_id"
    
    _columns = {
        'name':fields.char(
                    'Procedencia del Paciente', 
                    required=True, 
                    help='Nombre del Paciente.'
                    ),
        'partner_id': fields.many2one(
                    'res.partner', 
                    'Paciente', 
                    ondelete='restrict',
                    required=True,
                    readonly=False,
                    ),
        'active': fields.boolean(
                    'Activo',
                    readonly=True, 
                    help='Estatus del registro Activado-Desactivado.'),
    }
    
    _defaults = {
        'active':True,
    }
    
    
    def create(self, cr, uid, vals, context=None):
        vals.update({
            'name':vals['name'].upper(),
            
            })
        return super(cli_procedencia_paciente, self).create(cr, uid, vals, context=context)
        
    def write(self, cr, uid, ids, vals, context=None):
        if 'name' in vals.keys():
            vals.update({'name':vals['name'].upper(),})
        return super(cli_procedencia_paciente, self).write(cr, uid, ids, vals, context=context)
    
