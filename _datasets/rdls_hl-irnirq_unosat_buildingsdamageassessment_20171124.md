---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-north-of-sarpol-e-zahab-county-iran-2737
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-north-of-sarpol-e-zahab-county-iran-2737
dataset_id: rdls_hl-irnirq_unosat_buildingsdamageassessment_20171124
description: 'This map illustrates satellite-detected damaged and potentially damaged
  buildings and the related density of damage in the areas north of Sarpol-e-Zahab
  county in Kermanshah province, Iran following the M 7.3 earthquake that struck the
  area on the 12 November 2017. The analysis was carried out comparing a post-event
  Pleiades image acquired on the 16 November 2017 with a pre-event WorldView3 image
  of 24 July 2017. The results indicate damage across several localities and villages
  in this zone and about 3300 structures were identified as potentially damaged (e.g.
  362 in Koeeke Hasan; 148 in Tapamaran and 98 in Jaberi). This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-north-of-sarpol-e-zahab-county-iran-2737]'
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
  description: UNOSAT analysts compared pre-event and post-event satellite imagery
    to identify structural damage caused by the M 7.3 earthquake. Building footprints
    and damage status were extracted through visual interpretation of high-resolution
    satellite data, with confidence levels assigned to damage classifications and
    field validation conducted where possible.
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
- href: https://data.humdata.org/dataset/buildings-damage-assessment-related-density-north-of-sarpol-e-zahab-county-iran-2737
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected damaged and potentially damaged buildings following
      the M 7.3 earthquake, with approximately 3300 structures identified as damaged
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
  description: Buildings Damage Assessment & Related Density North of Sarpol-e-Zahab
    County, Iran (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/EQ20171112IRQ/EQ20171112IRQ_gdb.zip
  format: Geodatabase
  id: resource_09aa0bbc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20171112IRQ_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Buildings Damage Assessment & Related Density North of Sarpol-e-Zahab
    County, Iran (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IQ/EQ20171112IRQ/EQ20171112IRQ_shp.zip
  format: null
  id: resource_fabc48e1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20171112IRQ_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-irnirq_unosat_buildingsdamageassessment_20171124
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  - IRN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-24'
temporal_resolution: null
title: Buildings Damage Assessment & Related Density North of Sarpol-e-Zahab County,
  Iran
version: null
vulnerability: null
---
