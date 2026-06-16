---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Disaster preparedness centre
    url: https://data.humdata.org/dataset/1999-2013-tally-of-internaly-displaced-persons-resulting-from-natural-disasters
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Kenya Open Data Initiative (inactive)
  url: https://data.humdata.org/dataset/1999-2013-tally-of-internaly-displaced-persons-resulting-from-natural-disasters
creator:
  affiliation: null
  email: null
  name: Kenya Open Data Initiative (inactive)
  url: https://data.humdata.org/dataset/1999-2013-tally-of-internaly-displaced-persons-resulting-from-natural-disasters
dataset_id: rdls_lss-ken_kodi_tallyinternalydisplacedpe_2003
description: 'This data-set shows the Number of people affected by Disasters in Kenya.
  It is based on the National Disaster inventory which is a record of Natural Disasters
  including floods, thunderstorms, forest fires, mudslides and disease outbreaks..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/1999-2013-tally-of-internaly-displaced-persons-resulting-from-natural-disasters]'
details: This dataset has been sourced from Kenya open data portal
exposure: []
hazard: null
license: CC0-1.0
lineage:
  description: Post-event impact data compiled from the National Disaster inventory
    maintained by Kenya's National Disaster preparedness centre, recording internally
    displaced persons counts resulting from multiple natural disaster types (floods,
    thunderstorms, forest fires, mudslides, and disease outbreaks) across Kenya.
  sources:
  - id: source_1
    license: null
    name: National Disaster preparedness centre
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/1999-2013-tally-of-internaly-displaced-persons-resulting-from-natural-disasters
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons resulting from flood disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons resulting from thunderstorm disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons resulting from forest fire disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_wildfire
      intensity_measure: FWI:-
      process: null
      trigger: null
      type: wildfire
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons resulting from mudslide disasters
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_4
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
purpose: Registry
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This dataset shows the total recorded number of people affected by
    disasters in Kenya. It is based on the National Disaster inventory, which is a
    record of Natural Disasters including floods, thunderstorms, forest fires, mudslides
    and disease outbreaks.
  download_url: https://data.humdata.org/dataset/1d7193a5-52ed-4e89-9d14-fb62f2ca8e9c/resource/e6b336ba-7e8d-4a05-9162-89071272e103/download/national_natural_disaster_inventory.csv
  format: null
  id: resource_e6b336ba
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: National_Natural_Disaster_Inventory.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kenya - Tally of Internaly displaced persons resulting from natural
    disasters (Shapefile)
  download_url: https://data.humdata.org/dataset/1d7193a5-52ed-4e89-9d14-fb62f2ca8e9c/resource/5894a78f-2fcb-4977-8ab5-3614909cc572/download/national_natural_disaster_inventory.zip
  format: null
  id: resource_5894a78f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: National_Natural_Disaster_Inventory.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ken_kodi_tallyinternalydisplacedpe_2003
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2013-12-31'
  start: '2003-01-01'
temporal_resolution: null
title: Kenya - Tally of Internaly displaced persons resulting from natural disasters
version: null
vulnerability: null
---
