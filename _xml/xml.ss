(require scheme/file)

(require xml)
(xml->xexpr (document-element
                 (read-xml (open-input-string
                            (file->string "/home/rags/_xml/xml.xml"))))) 