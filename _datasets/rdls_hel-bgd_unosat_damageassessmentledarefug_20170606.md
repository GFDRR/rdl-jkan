---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-leda-refugee-camp-nhilla-union-bangladesh
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-leda-refugee-camp-nhilla-union-bangladesh
dataset_id: rdls_hel-bgd_unosat_damageassessmentledarefug_20170606
description: 'This map illustrates satellite-detected potentially affected shelters
  in Leda refugee camp in Nhilla Union, Cox s Bazar District, and Chittagong Division
  of Bangladesh. About 18,350 people are registered in this camp. The UNITAR-UNOSAT
  analysis used a Pleiades satellite image acquired 05 June 2017 and could identify
  215 possible damaged shelter structures within the extent of the camp. Kindly note
  that the number of damaged shelters could have been underestimated as some groups
  of shelter structures might be identified as one structure. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR - UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-leda-refugee-camp-nhilla-union-bangladesh]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Shelter structures in Leda refugee camp
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
      quantity_kind: count
      unit: count
- asset_type:
    description: Registered refugee population in Leda camp (18,350 people)
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared Pleiades satellite imagery acquired on 5 June
    2017 with reference imagery to detect structural changes in Leda refugee camp
    shelters following a tropical cyclone event on 29 May 2017. Visual interpretation
    identified 215 potentially damaged shelter structures within the camp extent,
    with results delivered as vector geodatabase and shapefile formats containing
    shelter geometry and damage status.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-leda-refugee-camp-nhilla-union-bangladesh
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct shelter damage from tropical cyclone detected via satellite
      imagery (215 damaged structures)
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
  description: Damage Assessment in Leda Refugee Camp, Nhilla Union, Bangladesh (Zipped
    geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/TC20170529BGD/TC20170529BGD_gdb.zip
  format: Geodatabase
  id: resource_e47064f2
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
  description: Damage Assessment in Leda Refugee Camp, Nhilla Union, Bangladesh (Zipped
    shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/BD/TC20170529BGD/TC20170529BGD_SHP.zip
  format: null
  id: resource_0c35c623
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170529BGD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bgd_unosat_damageassessmentledarefug_20170606
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
  start: '2017-06-06'
temporal_resolution: null
title: Damage Assessment in Leda Refugee Camp, Nhilla Union, Bangladesh
version: null
vulnerability: null
---
