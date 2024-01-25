# Adding More Conductance Values to [Master JSON File](../data/conductance_values.json)

### APPENDING CONTACT CONDUCTANCE VALUES:

Contact conductances are seperated by how much pressure there is between each surface: *high*, medium (*mid*), and *low*.

The name for the two surfaces should be in *alphabetical order connected with a dash*.\
**EXAMPLE:** If the surfaces are *steel* and *aluminum*, then the name for this contact is *"aluminum-steel"*

The contact values are a *two element (float or integer) array*.
The *first element* is the contact with a *LOW k-value* and the *second element* for a *HIGH k-value*.

---

### APPENDING MATERIAL CONDUCTANCE VALUES:

Adding values here is straightforward, just the *name of the material* and its *corresponding thermal resistance*.

