---
attributions:
- entity:
    affiliation: null
    email: null
    name: GLOBHE (Crowddroning)
    url: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-chikwawa-malawi
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-chikwawa-malawi
creator:
  affiliation: null
  email: null
  name: Globhe Drones
  url: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-chikwawa-malawi
dataset_id: rdls_el-mwi_globhe_posttropicalstormchalanem_20210110
description: 'Drone orthomosaic. Post Tropical Storm Chalane Mapping, Malawi conducted
  with Crowddroning by GLOBHE. More maps and data available on demand upon request
  from locations globally at https://globhe.com/ MORE CROWDDRONING BY GLOBHE Webb:
  https://globhe.com/ Facebook: https://www.facebook.com/Crowddroning Twitter: https://twitter.com/globhedrones
  Instagram: https://www.instagram.com/globhedrones/ LinkedIn: https://www.linkedin.com/company/globhedrones/.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-chikwawa-malawi]'
details: null
exposure:
- asset_type:
    description: Building structures and infrastructure visible in post-event drone
      orthomosaic imagery
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Land cover and vegetation damage assessment from aerial imagery
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: Post-event drone orthomosaic imagery was collected by GLOBHE using
    crowddroning methodology over Chikwawa, Malawi following Tropical Storm Chalane
    to document and map direct damage to buildings and natural environment.
  sources:
  - id: source_1
    license: null
    name: GLOBHE (Crowddroning)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/post-tropical-storm-chalane-mapping-chikwawa-malawi
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Storm Chalane assessed via drone
      orthomosaic
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
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct damage to vegetation and natural environment from Tropical
      Storm Chalane
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Drone orthomosaic. Post Tropical Storm Chalane Mapping, Malawi conducted
    with Crowddroning by GLOBHE. More maps and data available on demand upon request
    from locations globally at https://globhe.com/
  download_url: https://www.dropbox.com/s/uou3cn722tgrzoy/Post%20Tropical%20Storm%20Chalane%20Mapping%2C%20Chikwawa%2C%20Malawi.tif?dl=1
  format: null
  id: resource_0a9cb594
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Orthomosaic map (TIFF)
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-mwi_globhe_posttropicalstormchalanem_20210110
spatial:
  bbox: null
  centroid: null
  countries:
  - MWI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-01-10'
temporal_resolution: null
title: Post Tropical Storm Chalane Mapping, Chikwawa, Malawi
version: null
vulnerability: null
---
