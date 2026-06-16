---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Planetary Response Network
  url: https://data.humdata.org/dataset/jamaica-and-haiti-hurricane-melissa-road-blockages
creator:
  affiliation: null
  email: null
  name: Planetary Response Network
  url: https://data.humdata.org/dataset/jamaica-and-haiti-hurricane-melissa-road-blockages
dataset_id: rdls_lss-htijam_planetary_respo_hurricanemelissaroadblock_202511
description: 'This is a point dataset of road blockages in Jamaica and Haiti following
  Hurricane Melissa. The road blockages are marked by a single point, alongside the
  type of damage e.g. debris, flooding or coastal damage. The data is held in a shapefile
  format using the WGS 84 EPSG: 4326 projection. The Hurricane Melissa 2025 project
  data was collected via crowdsourcing on the Zooniverse platform.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/jamaica-and-haiti-hurricane-melissa-road-blockages]'
details: "We thank 'Imagery \xC2\xA9 2025 Planet Labs Inc.' for the satellite imagery,\
  \ and HOT for the roads, airports and ports vector layers used for this project."
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event road damage assessment conducted by crowdsourced volunteers
    analyzing PlanetScope 3m resolution satellite imagery acquired after Hurricane
    Melissa. Volunteers categorized road blockages and bridge damage across Jamaica
    and Haiti, with damage types classified as debris, flooding, or coastal damage.
    Results compiled into point shapefiles with damage type attributes.
  sources:
  - id: source_1
    license: null
    name: Planetary Response Network
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/jamaica-and-haiti-hurricane-melissa-road-blockages
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct road infrastructure damage from Hurricane Melissa assessed
      via post-event imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://www.zooniverse.org/projects/alicemead/planetary-response-network-hurricane-melissa-2025
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica and Haiti - Hurricane Melissa Road Blockages (Jamaica - Road
    Damage)
  download_url: https://data.humdata.org/dataset/34bd6a03-a5ee-4296-a842-3ed80e494b49/resource/dad7ac64-f8d5-42c6-b1b5-d293056ce6a3/download/jamaica_road_damage.zip
  format: null
  id: resource_dad7ac64
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jamaica_road_damage.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Jamaica and Haiti - Hurricane Melissa Road Blockages (Haiti - Road
    Damage)
  download_url: https://data.humdata.org/dataset/34bd6a03-a5ee-4296-a842-3ed80e494b49/resource/5defa00c-1171-44c4-ac14-3219e122c7f9/download/haiti_road_damage.zip
  format: null
  id: resource_5defa00c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: haiti_road_damage.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-htijam_planetary_respo_hurricanemelissaroadblock_202511
spatial:
  bbox: null
  centroid: null
  countries:
  - JAM
  - HTI
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-11-04'
  start: '2025-11-02'
temporal_resolution: null
title: Jamaica and Haiti - Hurricane Melissa Road Blockages
version: null
vulnerability: null
---
