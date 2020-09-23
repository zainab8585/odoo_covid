# -*- coding: utf-8 -*-

from odoo import models, fields, api

class covid_19(models.Model):
    _name = 'covid_19.covid_19'
    _order = 'id desc'

    source = fields.Char("Source", required=True)
    date = fields.Datetime("Date time ", required=True, default=fields.Datetime.now())
    country_id = fields.Many2one("res.country", required=True)
    infected = fields.Integer("Number of infected", required=True, default=0)
    recovred = fields.Integer("Number of recovered", required=True, default=0)
    decseaced = fields.Integer("Number of decseaced", required=True, default=0)
    total_infected = fields.Integer("Total infected"
                                     , compute='set_total_infected', required=True, default=0)
    total_recoverd = fields.Integer("Total recovered"
                                     , compute="set_total_recovred",required=True, default=0)
    total_decseaced = fields.Integer("Total decseaced "
                                      , compute="set_total_decseaced",required=True, default=0)
    @api.depends('infected')
    def set_total_infected(self):
        print('self')
        print(self)
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
            ]
            print('4-----------',data.date)
            # print(self.date)
            records = self.search(domain)
            print('records')
            print(records)
            Infected = records.mapped('infected')
            print("Infected.....")
            print(Infected)
            print(sum(Infected))
            data.total_infected = sum(Infected) + data.infected

    @api.depends('recovred')
    def set_total_recovred(self):
        print('self')
        print(self)
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
            ]
            print('4-----------',data.date)
            records = self.search(domain)
            print('records')
            print(records)
            Recovred = records.mapped('recovred')
            print("Recovred.....")
            print(Recovred)
            print(sum(Recovred))
            data.total_recoverd = sum(Recovred) + data.recovred


    @api.depends('decseaced')
    def set_total_decseaced(self):
        print('self')
        print(self)
        for data in self:
            domain = [
                ('country_id', '=', data.country_id.id),
                ('date', '<', data.date),
            ]
            print('4-----------',data.date)
            records = self.search(domain)
            print('records')
            print(records)
            Decseaced = records.mapped('decseaced')
            print("Decseaced.....")
            print(Decseaced)
            print(sum(Decseaced))
            data.total_decseaced = sum(Decseaced) + data.decseaced