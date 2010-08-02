require 'rexml/document'
p REXML::Document.new(File.read("xml.xml")).to_s
