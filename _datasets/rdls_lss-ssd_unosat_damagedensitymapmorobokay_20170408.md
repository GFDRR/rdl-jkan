---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNITAR-UNOSAT
    url: https://data.humdata.org/dataset/damage-density-map-morobo-kaya-road-nahr-yei-district-south-sudan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-map-morobo-kaya-road-nahr-yei-district-south-sudan
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-density-map-morobo-kaya-road-nahr-yei-district-south-sudan
dataset_id: rdls_lss-ssd_unosat_damagedensitymapmorobokay_20170408
description: 'This map illustrates satellite-detected damage density along the road
  connecting the cities of Morobo and Koya, Nahr Yei district, Central Equatoria,
  South Sudan. Using satellite imagery acquired 05 March 2017, UNITAR - UNOSAT identified
  a total of around 7,800 destroyed structures within the analysis extent of the current
  map (approximately 600 square kilometers). The whole analysis over the Nahr Yei
  district covers an area of approximately 3,640 square kilometers, and the results
  show over 18,300 destroyed structures. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-density-map-morobo-kaya-road-nahr-yei-district-south-sudan]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard: null
license: CC-BY-SA-4.0
lineage:
  description: Damage assessment derived from visual interpretation of satellite imagery
    acquired 05 March 2017, comparing imagery to identify destroyed structures. Analysts
    reviewed imagery and classified damage density across approximately 3,640 square
    kilometers of Nahr Yei district.
  sources:
  - id: source_1
    license: null
    name: UNITAR-UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-density-map-morobo-kaya-road-nahr-yei-district-south-sudan
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected destroyed structures from conflict-related damage
      along Morobo-Kaya road corridor
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: South Sudan - Damage density map in Morobo-Kaya road, Nahr Yei district
    (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Yei_5Mar2017.gdb.zip
  format: Geodatabase
  id: resource_bc315a1f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Yei_5Mar2017.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan - Damage density map in Morobo-Kaya road, Nahr Yei district
    (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Yei_5Mar2017_shp.zip
  format: null
  id: resource_f7ef30ff
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Yei_5Mar2017_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ssd_unosat_damagedensitymapmorobokay_20170408
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-04-08'
temporal_resolution: null
title: South Sudan - Damage density map in Morobo-Kaya road, Nahr Yei district
version: null
vulnerability: null
---
