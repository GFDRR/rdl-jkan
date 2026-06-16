---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-gaza-city-gaza-strip-occupied-palestinian-ter-july-31-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-gaza-city-gaza-strip-occupied-palestinian-ter-july-31-2014
dataset_id: rdls_el-pse_unosat_geodatadamageassessmentci_20140731
description: 'This map illustrates satellite-detected damage and destruction in central
  Gaza City, Gaza Strip, resulting from ongoing violence in the area. Using a satellite
  image collected 25 July 2014 by the Pleiades satellite, and compared with a pre-crisis
  Pleiades image collected 6 July 2014, UNOSAT analysis has identified 133 destroyed
  structures, 179 severely damaged structures, and 218 moderately damaged structures.
  In addition, 126 craters on roads and in agricultural and non-urbanized areas are
  also visible as of 25 July 2014. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to UNITAR/UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-gaza-city-gaza-strip-occupied-palestinian-ter-july-31-2014]'
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
    description: Building stock classified by damage severity (destroyed, severely
      damaged, moderately damaged)
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
    description: Road infrastructure with crater damage counts
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared pre-crisis and post-crisis Pleiades satellite
    imagery collected on 6 July 2014 and 25 July 2014 respectively to identify and
    classify damage to buildings and infrastructure in Gaza City. Damage was categorized
    into three severity levels (destroyed, severely damaged, moderately damaged) for
    structures and counted as craters for roads and non-urbanized areas. Results were
    compiled into spatial vector datasets with damage classification attributes.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-gaza-city-gaza-strip-occupied-palestinian-ter-july-31-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from conflict-related violence
      with satellite-detected destruction and damage classification
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage from conflict-related violence with
      crater counts on roads and agricultural areas
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
  description: Palestine - Geodata of Damage Assessment in Gaza City, Gaza Strip -
    Occupied Palestinian Territory (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PS/CE20140715PSE/CE20140715PSE.SHP.zip
  format: null
  id: resource_e15bbe24
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140715PSE.SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - Geodata of Damage Assessment in Gaza City, Gaza Strip -
    Occupied Palestinian Territory (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PS/CE20140715PSE/CE20140715PSE.gdb.zip
  format: null
  id: resource_bc88399c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140715PSE.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_geodatadamageassessmentci_20140731
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-07-31'
temporal_resolution: null
title: Palestine - Geodata of Damage Assessment in Gaza City, Gaza Strip - Occupied
  Palestinian Territory
version: null
vulnerability: null
---
