---
attributions:
- entity:
    affiliation: null
    email: lloeschner@worldbank.org
    name: Lukas Loeschner
    url: null
  id: '0'
  role: world_bank_team_lead
- entity:
    affiliation: null
    email: mamadio@worldbank.org
    name: Mattia Amadio
    url: null
  id: '1'
  role: author
catalog: null
contact_point:
  affiliation: null
  email: lloeschner@worldbank.org
  name: Lukas Loeschner
  url: null
creator:
  affiliation: null
  email: mamadio@worldbank.org
  name: Mattia Amadio
  url: null
dataset_id: rdls_exp-ssd_gfdrr_assetexposure
description: Collection of exposure data from Open Street Map, OCHA and World Bank,
  representing location and type of settlments, land use, buildings, health facilities
  and roads.
details: "To better understand natural hazard and disaster risk, the World Bank and\
  \ Global Facility for Disaster Reduction and Recovery (GFDRR) supported the development\
  \ of new \uFB02uvial \uFB02ood, \uFB02ash \uFB02ood, drought, landslide, avalanche\
  \ and seismic risk information in Afghanistan, as well as a frst-order analysis\
  \ of the costs and benefts of resilient reconstruction and risk reduction strategies.\
  \ This publication describes the applied methods and main results of the project."
exposure:
- asset_type: null
  category: buildings
  id: rdls_exp-ssd_gfdrr_assetexposure_exp
  metrics:
  - dimension: structure
    id: rdls_exp-ssd_gfdrr_assetexposure_m1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: South Sudan Multi-hazard risk assessment
  url: null
publisher:
  affiliation: null
  email: null
  name: GFDRR
  url: https://www.gfdrr.org
purpose: The results of the analysis contribute to the production of knowledge for
  disaster risk management (DRM) to support the World Bank's operational teams in
  their in-country engagements. Specifcally, the key fndings of this study allow to
  rank South Sudan states in terms of natural disasters risk, and to identify the
  most critical components for each area. The output of this assessment includes a
  geodatabase which contains both the key primary data and all the resulting maps
  produced by the analysis, allowing risk analysts and managers to explore them in
  detail using GIS software.
referenced_by:
- author_names:
  - Rina Meutia
  - Lukas Loeschner
  - Makiko Watanabe
  - Meskerem Brhane
  - Mattia Amadio
  date_published: '2020-09-24'
  doi: null
  id: '0'
  name: 'Disasters, Conflict, and Displacement : Intersectional Risks in South Sudan
    (Vol. 2)'
  url: http://documents1.worldbank.org/curated/en/570701601009027965/pdf/Summary.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Location and ranking of settlements from OCHA (2019)
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0042416/DR0053214/exp-ssd-settlements_ocha.zip
  format: gpkg
  id: '0'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Settlements
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Buildings, land use, and roads polygons from OpenStreetMap
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0042416/DR0053213/exp-ssd-osm.zip
  format: gpkg
  id: '1'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: South Sudan buildings, land use and roads
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Location and ranking of health facilities from World Bank (2009)
  download_url: https://datacatalogfiles.worldbank.org/ddh-published/0042416/DR0053215/exp-ssd-health_wb.zip
  format: gpkg
  id: '2'
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Health facilities
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_gfdrr_assetexposure
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
title: South Sudan Asset exposure
version: '2019'
vulnerability: null
---
