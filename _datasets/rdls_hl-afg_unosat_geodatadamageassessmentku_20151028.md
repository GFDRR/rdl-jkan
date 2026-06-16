---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kunduz-area-kunduz-province-afghanistan-october-28-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kunduz-area-kunduz-province-afghanistan-october-28-2015
dataset_id: rdls_hl-afg_unosat_geodatadamageassessmentku_20151028
description: "This map illustrates satellite-detected potential damaged structures\
  \ in the city of Kunduz in Afghanistan, approximately 200 kilometers from the epicenter\
  \ of the 26 October 2015 earthquake. Using a Pl\xE9iades satellite image acquired\
  \ 28 October 2015 and a WorldView-2 image acquired 21 October 2015, UNITAR/UNOSAT\
  \ did not observe major destruction related to the earthquake in Kunduz. However,\
  \ a total of 12 potentially affected structures in Kunduz were identified. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kunduz-area-kunduz-province-afghanistan-october-28-2015]"
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "UNOSAT analysts compared Pl\xE9iades satellite imagery acquired 28\
    \ October 2015 with WorldView-2 imagery from 21 October 2015 to detect structural\
    \ changes and identify potentially damaged buildings in Kunduz city following\
    \ the 26 October 2015 earthquake. A total of 12 potentially affected structures\
    \ were identified through visual interpretation of satellite imagery, representing\
    \ preliminary analysis not yet validated in the field."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-kunduz-area-kunduz-province-afghanistan-october-28-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected potentially damaged structures in Kunduz city
      from the 26 October 2015 earthquake
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
  description: Geodata of Damage Assessment of Kunduz Area, Kunduz Province, Afghanistan
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/AF/EQ20151026AFG/EQ20151026AFG_shp.zip
  format: null
  id: resource_cfad8c3e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20151026AFG_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Kunduz Area, Kunduz Province, Afghanistan
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/AF/EQ20151026AFG/EQ20151026AFG.gdb.zip
  format: null
  id: resource_a895bc31
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20151026AFG.gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-afg_unosat_geodatadamageassessmentku_20151028
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-28'
temporal_resolution: null
title: Geodata of Damage Assessment of Kunduz Area, Kunduz Province, Afghanistan
version: null
vulnerability: null
---
