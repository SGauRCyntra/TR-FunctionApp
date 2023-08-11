import logging
import azure.functions as func

from .anaplan import anaplan
from .qualitrics import qualitrics
from .suppliers import suppliers
from .OrderAddress import orderAddress
from .createRawMaterial import createRawMaterial
from .createSupplierRawMaterial import createSupplierRawMaterial
from .updateSupplierRawMaterial import updateSupplierRawMaterial
from .shipToAddress import shipToAddress
from .getLocationSalesData import getLocationSalesData
from .itemTable import itemTable
from .getLocations import getLocations
from .loadProduction import loadProduction
from .testOrderAddress import testOrderAddress
from .assurx import assurx
from .complaints2 import complaints2
from .salesforce import salesforce

import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            file = req_body.get('file')
            body = req_body.get('body')

    if name:
        if name == "anaplan":
            blob = anaplan(file)
            status_code, status = blob.process()
            return func.HttpResponse(status,status_code=status_code)
        elif name == "qualtrics":
            blob = qualitrics(file)
            status_code, status = blob.process()
            return func.HttpResponse(status,status_code=status_code,  mimetype="application/json")
        elif name == "suppliers":
            blob = suppliers(file, body)
            status_code, payload = blob.process()
            return func.HttpResponse(json.dumps({"Vendor Details" : payload}),status_code=status_code,  mimetype="application/json")
        elif name == "orderAddress":
            blob = orderAddress(body)
            status_code, payload = blob.process()
            return func.HttpResponse(json.dumps({"Order Address" : payload}),status_code=status_code,  mimetype="application/json")
        elif name == "testOrderAddress":
            blob = testOrderAddress(file)
            status_code, payload = blob.process()
            return func.HttpResponse(json.dumps({"Order Address" : payload}),status_code=status_code,  mimetype="application/json")
        elif name == "createRawMaterial":
            blob = createRawMaterial(body)
            status_code, payload = blob.process()
            return func.HttpResponse(json.dumps({"Orders" : payload}),status_code=status_code,  mimetype="application/json")
        elif name == "createSupplierRawMaterial":
            logging.info(body)
            blob = createSupplierRawMaterial(body)
            status_code, payload = blob.process()
            return func.HttpResponse(json.dumps({"Orders" : payload}),status_code=status_code,  mimetype="application/json")
        elif name == "updateSupplierRawMaterial":
            logging.info(body)
            blob = updateSupplierRawMaterial(body)
            status_code, payload = blob.process()
            return func.HttpResponse(json.dumps({"Orders" : payload}),status_code=status_code,  mimetype="application/json")
        elif name == "shipToAddress":
            logging.info(body)
            blob = shipToAddress(body)
            status_code, payload = blob.process()
            return func.HttpResponse(payload, status_code=status_code)
        elif name == "getLocationSalesData":
            logging.info(body)
            blob = getLocationSalesData(body)
            status_code, payload = blob.process()
            return func.HttpResponse(payload, status_code=status_code)
        elif name == "demandPlanning":
            logging.info(body)
            blob = itemTable(body)
            status_code, payload = blob.process()
            return func.HttpResponse(payload, status_code=status_code)
        elif name == "getLocations":
            logging.info(body)
            blob = getLocations(body)
            status_code, payload = blob.process()
            return func.HttpResponse(payload, status_code=status_code)
        elif name == "loadProduction":
            logging.info(body)
            blob = loadProduction(body)
            status_code, payload = blob.process()
            return func.HttpResponse(payload, status_code=status_code)
        elif name == "complaints":
            # logging.info(body)
            blob = assurx(body)
            status_code, payload = blob.process()
            return func.HttpResponse(payload, status_code=status_code, mimetype="application/json")
        elif name == "salesforce":
            logging.info(body)
            blob = salesforce(body)
            status_code, payload = blob.process()
            return func.HttpResponse(payload, status_code=status_code, mimetype="application/json")
        elif name == "complaints2":
            # logging.info(body)
            blob = complaints2(body)
            status_code, payload = blob.process()
            return func.HttpResponse(json.dumps(payload), status_code=status_code, mimetype="application/json")
        else:
            return func.HttpResponse(
                "Filename Not valid",
                status_code=404
            )