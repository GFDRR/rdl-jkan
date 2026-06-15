---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNEP-GRID
    url: https://unepgrid.ch/en
  id: '1'
  role: publisher
- entity:
    affiliation: null
    email: null
    name: UNEP-GRID
    url: https://unepgrid.ch/en
  id: '2'
  role: creator
- entity:
    affiliation: null
    email: mamadio@worldbank.org
    name: Mattia Amadio
    url: null
  id: '3'
  role: contact_point
- entity:
    affiliation: null
    email: null
    name: CDRI
    url: https://cdri.world/
  id: '4'
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
creator:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
dataset_id: rdls_exp-giri_globalbuildingexposure
description: Datasets containing building footprint distribution at high resolution
  for exposure analysis at the global scale, categorized as residential, non-residential,
  and total buildings.
details: Building exposure datasets provide spatial distribution of building footprints
  globally, classified by use type (residential vs. non-residential). These datasets
  are essential for assessing the built environment exposure to natural hazards and
  estimating potential losses.
exposure:
- asset_type: null
  category: buildings
  id: rdls_exp-giri_globalbuildingexposure_exp
  metrics:
  - dimension: structure
    id: rdls_exp-giri_globalbuildingexposure_m1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Global Infrastructure Risk Model and Resilience Index (GIRI)
  url: https://giri.unepgrid.ch/
publisher:
  affiliation: null
  email: null
  name: UNEP-GRID
  url: https://unepgrid.ch/en
purpose: null
referenced_by:
- author_names:
  - T. Pillar
  - A. Benvenuti
  - A. De Bono
  date_published: '2023-08-31'
  doi: null
  id: reference_24asd
  name: The GIRI global building exposure model (BEM)
  url: https://giri.unepgrid.ch/sites/default/files/2023-09/GIRI_BEM_report_UNIGE.pdf
resources:
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Spatial distribution of residential building footprints
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: BLD_RES
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Residential buildings
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Spatial distribution of non-residential building footprints (commercial,
    industrial, institutional)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: BLD_NONRES
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Non-residential buildings
- access_url: https://giri.unepgrid.ch/map
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Spatial distribution of all building footprints (residential and non-residential
    combined)
  download_url: https://giri.unepgrid.ch/map
  format: GeoTIFF
  id: BLD_TOTAL
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Total buildings
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-giri_globalbuildingexposure
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Global building exposure
version: '1'
vulnerability: null
---
