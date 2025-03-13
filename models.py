# -*- coding: utf-8 -*-
from odoo import models, fields, api

# class clientspec(models.Model):
#     _name = 'clientspec.clientspec'
#     name = fields.Char()

class Client(models.Model):
    _name = 'clientspec.client'
    _description = "Client grossiste"

    name = fields.Char(string="Nom_Client", required=True)
    is_local = fields.Boolean(string="Local ?", default=False)
    client_type = fields.Selection([ ('individual', 'Particulier'),
            ('public', 'Entreprise Publique'),
            ('private', 'Entreprise Privée')],string="Type de Client",
        default='individual',
        required=True #required = true rends le champs obligatoire
        )
    commande_ids = fields.One2many(
        'clientspec.commande', 'client_id', string="Commandes"
    )
    assurance_ids = fields.Many2many(
    'clientspec.assurance', 'client_assurance_rel',
    'client_id', 'assurance_id',
    string="Assurances"
    )

class Commande(models.Model):
    _name = 'clientspec.commande'
    _description = "Commandes speciales"

    name = fields.Char(string="IdCommande", required=True)
    date = fields.Date()
    price = fields.Float(digits=(6, 2), help="le prix")
    client_id = fields.Many2one(
        'clientspec.client', ondelete='cascade', string="Client", required=True
    )

class Assurance(models.Model):
    _name = 'clientspec.assurance'
    _description = "assurance client grossiste"

    label = fields.Char(string="IdAssurance", required=True)
    dateSouscription = fields.Date()
    piece = fields.Binary()
    #client_id = fields.Many2one(
     #   'clientspec.client', ondelete='cascade', string="Client", required=True
    #)
    client_ids = fields.Many2many(
    'clientspec.client', 'client_assurance_rel',
    'assurance_id', 'client_id',
    string="Clients"
    )
