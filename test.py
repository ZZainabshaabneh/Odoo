from odoo import models, fields, api
import time
class Config(models.Model):
    _name = 'sk_config'
    _description = 'sk_config'
    name=fields.Char()
    state = fields.Char("state")
    binary=fields.Binary(width="120")
    txt = fields.Text("Billboard Reservation")
    maintaine = fields.Boolean("Check Maintainable", default=True) 
    avaliable = fields.Boolean("Check Available", default=True) 
    Billtype = fields.Many2one('sk_billtype')
    city = fields.Many2one('sk_city')
    BBCODE=fields.Char("BBCODE")
    shape= fields.Selection([('horizental','Horizental'),('vertical','Vertical')])
    BB=fields.Char("BB Space M^2")
    width=fields.Float("Width")
    height=fields.Float("Height")
    district = fields.Many2one('sk_district')
    location = fields.Many2one('sk_location')
    cat= fields.Selection([('regular','Regular'),('prime-مستوى أول','prime-مستوى أول')])
    mat= fields.Selection([('PVC','PVC'),('VINYL','VINYL'),('Steel','Steel'),('PVC-SP','PVC-SP')])

class BillType(models.Model):
    _name = 'sk_billtype'
    _description = 'sk_billtype'

    name = fields.Char("Billboard Type")


class District(models.Model):
    _name = 'sk_district'
    _description = 'sk_district'

    name = fields.Char(string="District")


class City(models.Model):
    _name = 'sk_city'
    _description = 'sk_city'

    name = fields.Char("City")
    district = fields.Many2one('sk_district')


class Location(models.Model):
    _name = 'sk_location'
    _description = 'sk_location'

    name = fields.Char("Location")
    district = fields.Many2one('sk_district')
    city = fields.Many2one('sk_city')
 

class Reservation(models.Model):
    _name = 'sk_reservation'
    _description = 'Reservation'

    invoice_id = fields.Many2one("account.move")
    invoice_user_id = fields.Many2one("res.users", related="invoice_id.invoice_user_id", readonly=True)
    Address = fields.Char(string="Address")
    Ordering_contact = fields.Char()

     # add_id = fields.Many2one("res.partner", string="Address")
     # street = fields.Many2one("res.partner", related="add_id.street", readonly=True)

    # ord_id = fields.Many2one("account.move", string="Ordering Contact")
    # ord_user_id = fields.Many2one("res.users", related="ord_id.ord_user_id", readonly=True)
 
    proname = fields.Char(string="Project Name")
    # ordname = fields.Char(string="Ordering Contact")
    # addname = fields.Char(string="Address")
    name = fields.Many2one('sk_location', string="Location")
    district = fields.Many2one('sk_district', string="District")
    city = fields.Many2one('sk_city', string="City")
    End_Date =fields.Date(default=time.strftime("%Y-12-31"))
    Start_Date =fields.Date(default=time.strftime("%Y-01-01"))
    table = fields.Selection([('IN MONTHS','IN MONTHS'),('IN DAYS','IN DAYS')],string="Table(Months/Days)")
    billboard_list = fields.Many2many("sk_config", string="Billboards")
    reservation_line_ids = fields.One2many(
        'sk_reservation',
        'parent_reservation_id',
        string="Reservation Lines"
    )
    parent_reservation_id = fields.Many2one('sk_reservation', string="Parent Reservation")
    

class Test(models.Model):
    _name = 'sk_test'
    _description = 'test.test'

    name = fields.Char()
    value = fields.Integer()
    billboard_list = fields.Many2many("sk_config")