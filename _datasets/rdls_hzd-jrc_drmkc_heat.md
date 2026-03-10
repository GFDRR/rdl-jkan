---
catalog: World Bank Data Catalog
contact_point:
  email: mamadio@worldbank.org
  name: Mattia Amadio
  url: https://www.gfdrr.org/en
creator:
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
dataset_id: rdls_hzd-jrc_drmkc_heat
description: Probabilistic modelling of extreme heat hazard
details: "Extreme Heat hazard is classified based on an existing and widely accepted\
  \ heat stress indicator, the Wet Bulb Globe Temperature (WBGT, in \xB0C) \u2013\
  \ more specifically the daily maximum WGBT. The WBGT has an obvious relevance for\
  \ human health, but it is relevant in all kinds of projects and sectors, including\
  \ infrastructure related, as heat stress affects personnel and stakeholders, and\
  \ therefore the design of buildings and infrastructure. Heat stress studies in the\
  \ scientific literature that make use of the WBGT apply thresholds of 28\xB0C and\
  \ 32\xB0C to categorise heat stress risk. The damaging intensity thresholds are\
  \ applied following this definition of slight/low (32\xB0C) heat stress."
exposure: null
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: extreme_temperature
  intensity: WBGT:c
  occurrence_range: 1/5 to 1/100 years
  processes: extreme_heat
license: CC0-1.0
loss: null
project: Development of a hazard screening protocol for Extreme Heat
publisher:
  name: Global Facility for Disaster Reduction and Recovery (GFDRR)
  url: https://www.gfdrr.org/en
purpose: To assess extreme heat hazard across regions using the Wet Bulb Globe Temperature
  (WBGT) indicator to support human health protection, infrastructure design, and
  heat stress risk management.
resources:
- coordinate_system: EPSG:4326
  description: "Probabilistic extreme heat hazard maps (the daily maximum of Wet Bulb\
    \ Globe Temperature, in \xB0C) for the 5-year return period, for Global "
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0050009/GLB_HS_RP5.tif
  format: geotiff
  id: Extreme_Heat_Hazard_RP5
  spatial_resolution: 10000
  title: Extreme Heat Hazard with 5 year Return Period
- coordinate_system: EPSG:4326
  description: "Probabilistic extreme heat hazard maps (the daily maximum of Wet Bulb\
    \ Globe Temperature, in \xB0C) for the 20-year return period, for Global "
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0050005/GLB_HS_RP20.tif
  format: geotiff
  id: Extreme_Heat_Hazard_RP20
  spatial_resolution: 10000
  title: Extreme Heat Hazard with 20 year Return Period
- coordinate_system: EPSG:4326
  description: "Probabilistic extreme heat hazard maps (the daily maximum of Wet Bulb\
    \ Globe Temperature, in \xB0C) for the 100-year return period, for Global "
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0050007/GLB_HS_RP100.tif
  format: geotiff
  id: Extreme_Heat_Hazard_RP100
  spatial_resolution: 10000
  title: Extreme Heat Hazard with 100 year Return Period
risk_data_type:
- hazard
schema: rdl-02
slug: rdls_hzd-jrc_drmkc_heat
spatial:
  countries:
  - GLO
  scale: global
title: Global Extreme Heat Hazard
version: '3'
vulnerability: null
---
