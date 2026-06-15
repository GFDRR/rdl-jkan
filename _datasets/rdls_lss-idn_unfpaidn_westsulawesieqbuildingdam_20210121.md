---
attributions:
- entity:
    affiliation: null
    email: null
    name: BNPB
    url: https://data.humdata.org/dataset/building-damage
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/building-damage
creator:
  affiliation: null
  email: null
  name: UNFPA Indonesia (inactive)
  url: https://data.humdata.org/dataset/building-damage
dataset_id: rdls_lss-idn_unfpaidn_westsulawesieqbuildingdam_20210121
description: 'This data contain of scatter location of building damage that extracted
  from geotag photos. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/building-damage]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Building damage locations were extracted from geotagged photographs
    collected in the field following the West Sulawesi earthquake. Point geometries
    with spatial coordinates (x, y, z) and temporal metadata (datetime, direction)
    were compiled into a shapefile representing direct observational damage records.
  sources:
  - id: source_1
    license: null
    name: BNPB
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/building-damage
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake assessed through geotagged
      photo observations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - West Sulawesi EQ - Building Damage (extracted from geotag
    photos of building damage in West Sulawesi)
  download_url: https://data.humdata.org/dataset/aac8c274-da9f-4444-9fb0-40a6f4f4f7a8/resource/c6b8f52c-684a-43f5-9cd1-2fc495bba006/download/bangunan_rusak.zip
  format: null
  id: resource_c6b8f52c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bangunan_rusak.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-idn_unfpaidn_westsulawesieqbuildingdam_20210121
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-01-21'
temporal_resolution: null
title: Indonesia - West Sulawesi EQ - Building Damage
version: null
vulnerability: null
---
