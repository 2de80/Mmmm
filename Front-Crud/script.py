selectedRow = None

def onFormSubmit(e):
    e.preventDefault()
    formData = readFormData()
    if selectedRow is None:
        insertNewRecord(formData)
    else:
        updateRecord(formData)
    resetForm()

def readFormData():
    formData = {}
    formData["productCode"] = document.getElementById("productCode").value
    formData["product"] = document.getElementById("product").value
    formData["qty"] = document.getElementById("qty").value
    formData["perPrice"] = document.getElementById("perPrice").value
    return formData

def insertNewRecord(data):
    table = document.getElementById("storeList").getElementsByTagName('tbody')[0]
    newRow = table.insertRow(table.length)
    cell1 = newRow.insertCell(0)
    cell1.innerHTML = data["productCode"]
    cell2 = newRow.insertCell(1)
    cell2.innerHTML = data["product"]
    cell3 = newRow.insertCell(2)
    cell3.innerHTML = data["qty"]
    cell4 = newRow.insertCell(3)
    cell4.innerHTML = data["perPrice"]
    cell4 = newRow.insertCell(4)
    cell4.innerHTML = '<button onClick="onEdit(this)">Editar</button> <button onClick="onDelete(this)">Eliminar</button>'

def onEdit(td):
    selectedRow = td.parentElement.parentElement
    document.getElementById("productCode").value = selectedRow.cells[0].innerHTML
    document.getElementById("product").value = selectedRow.cells[1].innerHTML
    document.getElementById("qty").value = selectedRow.cells[2].innerHTML
    document.getElementById("perPrice").value = selectedRow.cells[3].innerHTML

def updateRecord(formData):
    selectedRow.cells[0].innerHTML = formData["productCode"]
    selectedRow.cells[1].innerHTML = formData["product"]
    selectedRow.cells[2].innerHTML = formData["qty"]
    selectedRow.cells[3].innerHTML = formData["perPrice"]

def onDelete(td):
    if confirm('Desea eliminar este producto?'):
        row = td.parentElement.parentElement
        document.getElementById('storeList').deleteRow(row.rowIndex)
        resetForm()

def resetForm():
    document.getElementById("productCode").value = ''
    document.getElementById("product").value = ''
    document.getElementById("qty").value = ''
    document.getElementById("perPrice").value = ''
    selectedRow = None