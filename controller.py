def handleCreaGrafo(self, e):
    self._view.txt_result.controls.clear()

    self._model.buildGraph(uhgvug)
    self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente"))
    n, e = self._model.getDetails()
    self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {n}"))
    self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {e}"))

    self._view.update_page()