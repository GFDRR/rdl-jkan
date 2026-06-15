---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-kutupalong-refugee-camp-palong-khali-union-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-kutupalong-refugee-camp-palong-khali-union-bangladesh
dataset_id: rdls_lss-bgd_unosat_damageassessmentkutupalon_20170607
description: 'This map illustrates satellite-detected possible damaged shelter structures
  in Kutupalong Refugee Camp, Palong Khali Union and Cox Bazar District, Chittagong
  Division, Bangladesh. The UNITAR-UNOSAT analysis used Pleiades satellite imagery
  acquired the 6th and the 7th June 2017 as post-images. The UNITAR-UNOSAT analysis
  identified 1,105 possible damaged shelter structures within the extent of the camp.
  Kindly note that the number of possible shelter damaged structures could have been
  under or overestimated in some areas due to the cloud cover and the delimitation
  of the camp extent. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-in-kutupalong-refugee-camp-palong-khali-union-bangladesh]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre- and post-event Pleiades satellite imagery
    (6-7 June 2017) of Kutupalong Refugee Camp to detect structural changes and identify
    damaged shelters through visual interpretation and change detection. The resulting
    geodatabase contains mapped shelter damage polygons with area measurements, representing
    direct physical impacts from the cyclone event.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-kutupalong-refugee-camp-palong-khali-union-bangladesh
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct shelter damage from cyclone assessed via satellite imagery
      change detection
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Kutupalong Refugee Camp, Palong Khali Union, Bangladesh
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/TC20170529BGD/TC20170529BGD_gdb.zip
  format: Geodatabase
  id: resource_dd123461
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170529BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Kutupalong Refugee Camp, Palong Khali Union, Bangladesh
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/TC20170529BGD/TC20170529BGD_SHP.zip
  format: null
  id: resource_69464008
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170529BGD_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bgd_unosat_damageassessmentkutupalon_20170607
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-06-07'
temporal_resolution: null
title: Damage Assessment in Kutupalong Refugee Camp, Palong Khali Union, Bangladesh
version: null
vulnerability: null
---
