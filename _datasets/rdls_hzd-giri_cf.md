---
catalog: null
contact_point:
  email: mamadio@worldbank.org
  id: '3'
  name: Mattia Amadio
  url: null
creator:
  email: null
  id: '2'
  name: CIMA
  url: https://www.cimafoundation.org
dataset_id: rdls_hzd-GIRI_CF
description: Datasets containing probabilistic analysis of coastal flood water depth
  (m) at coastline due to storm surge, covering historical and climate change projections
  at the global scale.
details: "Storm surge hazard is modeled only along the coastline. The process involves\
  \ generating a grid along the coastline and 5km inland. In fact, no backwater effects\
  \ were modeled, this is only due to the continent\u2019s contour map (shapefile)\
  \ version used to create the grid mentioned on the coastline.\nIn this project,\
  \ Mediterranean tropical-like cyclones were not included in the hazard assessment\
  \ process. We considered only tropical cyclones as storms that develop in areas\
  \ of low pressure over tropical oceans, and that are associated with several hazards\
  \ such as strong winds and storm surge. These two hazards were assessed at a global\
  \ level but given that although tropical cyclones are formed along the North Atlantic\
  \ Ocean but do not occur in Europe, neither strong wings nor storm surge were modeled\
  \ for European countries. "
exposure: []
extra_attributions:
- email: null
  id: '4'
  name: CDRI
  role: resource_provider
  url: https://cdri.world/
hazard:
  calculation_method: simulated
  disaster_identifiers: ''
  hazard_analysis_type: probabilistic
  hazard_type: flood
  intensity: Wd:M
  occurrence_range: Return period 10 to 1,000 years
  processes: coastal_flood
  seasonality: ''
license: CC-BY-4.0
loss: null
project:
  name: Global Infrastructure Risk Model and Resilience Index (GIRI)
  url: https://giri.unepgrid.ch/
publisher:
  email: null
  id: '1'
  name: UNEP-GRID
  url: https://unepgrid.ch/en
purpose: null
resources:
- coordinate_system: EPSG:4326
  description: Collection of historical coastal flood and storm surge hazard maps
  download_url: https://hazards-data.unepgrid.ch/World_Storm_Surge.gpkg
  format: GeoPackage (gpkg)
  id: HST
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Coastal flood hazard (historical)
- coordinate_system: EPSG:4326
  description: Collection of projected coastal flood and storm surge hazard maps under
    climate change scenarios
  download_url: https://hazards-data.unepgrid.ch/World_Storm_Surge_CC.gpkg
  format: GeoPackage (gpkg)
  id: CC
  media_type: null
  spatial_resolution: null
  temporal: null
  title: Coastal flood hazard (climate change)
risk_data_type:
- hazard
schema: rdl-03
slug: rdls_hzd-GIRI_CF
spatial:
  countries:
  - GLO
  scale: global
title: Global coastal flood and storm surge hazard
version: '1'
vulnerability: null
---
