import panel as pn

from .panel import DataSetSelect

def app(doc):
    med = DataSetSelect()

    col = pn.Column(med.param.date_select, med.param.date_select1, med.param.data_select,
        med.param.country_select, med.outputs, med.view_data2, med.view_data)

    col.server_doc(doc)
