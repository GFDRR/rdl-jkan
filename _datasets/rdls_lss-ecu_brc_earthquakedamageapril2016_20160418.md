---
attributions:
- entity:
    affiliation: null
    email: null
    name: Ecuador Government
    url: https://data.humdata.org/dataset/ecuador-earthquake-damage-april-2016
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/ecuador-earthquake-damage-april-2016
creator:
  affiliation: null
  email: null
  name: British Red Cross Maps Team
  url: https://data.humdata.org/dataset/ecuador-earthquake-damage-april-2016
dataset_id: rdls_lss-ecu_brc_earthquakedamageapril2016_20160418
description: 'Damage data from Ecuador Government in google spreadsheets. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ecuador-earthquake-damage-april-2016]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Damage data from Ecuador Government post-event assessment reports were
    scraped and compiled into a structured spreadsheet by the British Red Cross Maps
    Team to document direct building impacts from the April 2016 earthquake.
  sources:
  - id: source_1
    license: null
    name: Ecuador Government
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ecuador-earthquake-damage-april-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from April 2016 earthquake in Ecuador
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Damage data from Ecuador Government in google spreadsheets: http://www.gestionderiesgos.gob.ec/informes-de-situacion-actual-terremoto-magnitud-7-8/'
  download_url: https://docs.google.com/spreadsheets/d/1klRixK82iRk1JnDOpAqKrry4VQiFcTGrfFZWr9ih-Z8/export?format=csv&id=1klRixK82iRk1JnDOpAqKrry4VQiFcTGrfFZWr9ih-Z8&gid=0
  format: Google Sheet
  id: resource_86babc61
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ecuador Earthquake damage
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ecu_brc_earthquakedamageapril2016_20160418
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-04-18'
temporal_resolution: null
title: Ecuador Earthquake damage - April 2016
version: null
vulnerability: null
---
