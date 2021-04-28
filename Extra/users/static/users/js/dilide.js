// Adicionar um atributo no link de confirmação para eliminar o registo
function fnIdselecionado(endereco, valor) {
  document.getElementById('btnConfirm').setAttribute('href', endereco);
  document.getElementById('selected').innerText = valor;
}
