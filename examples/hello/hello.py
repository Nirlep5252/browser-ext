from browser_ext.extension import ChromeExtension


extension = ChromeExtension(
    name="Hello World",
    version="1.0.0",
    description="This is a simple extension that says hello.",
    default_title="Hello World",
)
extension.add_popup("popup.html")
extension.build(overwrite=True)
