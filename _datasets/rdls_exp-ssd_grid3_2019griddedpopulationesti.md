---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Research Group
    url: https://data.humdata.org/dataset/south-sudan-2019-gridded-population-estimates
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development)
    url: https://data.humdata.org/dataset/south-sudan-2019-gridded-population-estimates
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/south-sudan-2019-gridded-population-estimates
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/south-sudan-2019-gridded-population-estimates
dataset_id: rdls_exp-ssd_grid3_2019griddedpopulationesti
description: 'These data were produced by the WorldPop Research Group at the University
  of Southampton. This work was funded by the Bill and Melinda Gates Foundation (BMGF)
  and the United Kingdom''s Department for International Development (OPP1182408).
  The primary intended use of these data was aiding the BMGF field teams. The modelling
  work was led by Claire Dooley with support from Chris Jochem and oversight by WorldPop
  director Andy Tatem and GRID3 lead Attila Lazar. The support of the whole WorldPop
  group is acknowledged, as well as the our GRID3 partners ( UNFPA , Columbia University
  and Flowminder ). We thank the teams at IOM and ACLED for their excellent work in
  collecting data and making it freely available. This work was supported with funding
  from the Bill & Melinda Gates Foundation (BMGF) and the United Kingdom''s Department
  for International Development (DFID). These data may be distributed using a Creative
  Commons Attribution Share-Alike 4.0 License. DATA DESCRIPTION This dataset provides
  population estimates for each settled 100m grid square in South Sudan. The grid
  square values were derived using the National Bureau of Statistics'' 2019 population
  projection estimates that were adjusted to account for displacement of people. The
  locations people have been displaced to were directly obtained from IOM''s Displacement
  Tracking Matrix (DTM). The locations people have been displaced from were derived
  using DTM and the Armed Conflict Locations and Events Database (ACLED). Numbers
  of displaced people per location were calculated using recorded numbers of international
  refugees and internally displaced persons. For further details, please, read SSD_population_v1_0_README.pdf
  Recommended citation WorldPop (School of Geography and Environmental Science, University
  of Southampton). 2020. South Sudan 2019 gridded population estimates from census
  projections adjusted for displacement, version 1.0. https://dx.doi.org/10.5258/SOTON/WP00659.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/south-sudan-2019-gridded-population-estimates]'
details: South Sudan 2019 gridded population estimates from census projections adjusted
  for displacement, version 1.0 For further details, please, read SSD_population_v1_0_README.pdf
  Contact release@worldpop.org for more information.
exposure:
- asset_type:
    description: Gridded population estimates at high spatial resolution, adjusted
      for internal displacement from census projections
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Census population data for South Sudan were spatially modeled by WorldPop
    using their standard gridding methodology and adjusted for internal displacement
    patterns. The resulting gridded population estimates at high spatial resolution
    were produced to support BMGF field operations and development planning in a context
    of significant population displacement.
  sources:
  - id: source_1
    license: null
    name: WorldPop Research Group
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/south-sudan-2019-gridded-population-estimates
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Top-down gridded population estimates (~100m) for South Sudan. This
    zip file contains a geotiff raster with estimates of total population size for
    each approximately 100 m grid cell across the study area.
  download_url: https://wopr.worldpop.org/download/23
  format: null
  id: resource_a14174fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SSD_population_v1_0_gridded.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'README: SSD Population v1.0. This README file provides information
    about the data included in the data release, how it was produced, source data
    that were used, and known assumptions and limitations of the results.'
  download_url: https://wopr.worldpop.org/download/24
  format: null
  id: resource_9a283e16
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SSD_population_v1_0_README.pdf
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_grid3_2019griddedpopulationesti
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: South Sudan 2019 gridded population estimates from census projections adjusted
  for displacement, version 1.0
version: null
vulnerability: null
---
