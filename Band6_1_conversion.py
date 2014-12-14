# ---------------------------------------------------------------------------
# Band6_1_conversion.py
# Usage: Band6_1_conversion <SingleOutput1> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Check out any necessary licenses
gp.CheckOutExtension("spatial")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Spatial Analyst Tools.tbx")

# Script arguments...
SingleOutput1 = sys.argv[1]
if SingleOutput1 == '#':
 SingleOutput1 = "C:\\Users\\Reuben\\AppData\\Local\\Temp\\SingleOutput1" # provide a default value if unspecified

# Local variables...

# Process: Single Output Map Algebra...
gp.SingleOutputMapAlgebra_sa("1282.71 / ln((666.09 / ((17.04 - 0)) * (D:\\GIS Database\\Singapore\\Landsat\\11_Oct_2002\\b6_1_extract - 0) / (255) + 1)) - 273", SingleOutput1, "")

