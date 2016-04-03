module Html = Dom_html

let start _ =
  let info = Html.getElementById "info" in
  info##innerHTML <- Js.string "wrote stuff in the textarea from ocaml";
  Js._false

let () =
  Html.window##onload <- Html.handler start
