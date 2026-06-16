---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-damaged-buildings-gathering-sites-over-gili-islands-lombok-utara-district-indonesia-2837
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-damaged-buildings-gathering-sites-over-gili-islands-lombok-utara-district-indonesia-2837
dataset_id: rdls_hl-idn_unosat_potentiallydamagedbuildin_20180808
description: 'This map illustrates satellite-detected potentially damaged buildings
  and gathering sites over Gili Islands as of 8 August 2018, after the 6.9 earthquake,
  that stroke Lombok Island on 5 August 2018. The analysis was conducted using a post-event
  Pleiades satellite image acquired on 8 August 2018. UNITAR-UNOSAT analysis identified
  minor damage over Gili Islands, 15 potentially damaged buildings, mainly observed
  in Gili Air and 6 potentially gatherings sites in Gili Trawangan island. Kindly
  note that Google Earth was used as Pre-event imagery, it might have decreased the
  confidence level of the analysis. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/potentially-damaged-buildings-gathering-sites-over-gili-islands-lombok-utara-district-indonesia-2837]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts conducted post-event damage assessment by comparing
    Pleiades satellite imagery (8 August 2018) with pre-event Google Earth imagery
    to identify structural damage from the 6.9 magnitude earthquake. Damage features
    were manually delineated and classified by confidence level, producing a vector
    dataset of potentially damaged buildings and gathering sites across Gili Islands.
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
- href: https://data.humdata.org/dataset/potentially-damaged-buildings-gathering-sites-over-gili-islands-lombok-utara-district-indonesia-2837
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected potentially damaged buildings (15 identified)
      in Gili Islands following the 6.9 magnitude earthquake
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Satellite-detected potentially damaged gathering sites (6 identified)
      in Gili Trawangan island following the earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
  description: Potentially Damaged Buildings & Gathering Sites over Gili Islands,
    Lombok Utara District, Indonesia (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/EQ20180805IDN/EQ20180805IDN_shp.zip
  format: null
  id: resource_8b82bdea
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20180805IDN_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-idn_unosat_potentiallydamagedbuildin_20180808
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
  start: '2018-08-08'
temporal_resolution: null
title: Potentially Damaged Buildings & Gathering Sites over Gili Islands, Lombok Utara
  District, Indonesia
version: null
vulnerability: null
---
