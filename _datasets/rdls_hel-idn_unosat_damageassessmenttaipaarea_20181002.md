---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-of-taipa-area-in-central-sulawesi-2845
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Worldview-2 satellite imagery
    url: https://data.humdata.org/dataset/damage-assessment-of-taipa-area-in-central-sulawesi-2845
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-taipa-area-in-central-sulawesi-2845
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-taipa-area-in-central-sulawesi-2845
dataset_id: rdls_hel-idn_unosat_damageassessmenttaipaarea_20181002
description: 'This map illustrates satellite-detected building damage assessment as
  of 02 October 2018, over Taipa area northeastern Palu city in Central Sulawesi following
  the 7.5 magnitude earthquake and subsequent tsunami of the 28th of September 2018.
  The analysis was conducted using a post-event Worldview-2 satellite image acquired
  2 October 2018. UNITAR-UNOSAT identified in the analysed area 399 potentially damaged
  structures. Taking into account the pre-building footprints provided by Humanitarian
  OpenStreetMap, this represents 10 % of the total number of structures within this
  analysed zone of Taipa.This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-of-taipa-area-in-central-sulawesi-2845]'
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
    description: Building footprints in Taipa area, northeastern Palu city, identified
      from Humanitarian OpenStreetMap
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
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: probabilistic
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre-event building footprints from Humanitarian
    OpenStreetMap with post-event Worldview-2 satellite imagery acquired 2 October
    2018 to identify structural damage in the Taipa area following the 28 September
    2018 earthquake and tsunami. Visual interpretation of satellite imagery changes
    detected 399 potentially damaged structures, representing 10% of the total building
    stock in the analysed zone.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Worldview-2 satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-of-taipa-area-in-central-sulawesi-2845
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from earthquake ground motion, identified
      as 399 potentially damaged structures via satellite imagery analysis
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Indonesia - Damage assessment of Taipa area in Central Sulawesi (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/EQ20181001IDN/EQ20181001IDN_shp.zip
  format: null
  id: resource_c364e960
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20181001IDN_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_damageassessmenttaipaarea_20181002
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
  start: '2018-10-02'
temporal_resolution: null
title: Indonesia - Damage assessment of Taipa area in Central Sulawesi
version: null
vulnerability: null
---
