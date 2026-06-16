---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-chardonnieres-commune-south-department-as-of-23-august-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-chardonnieres-commune-south-department-as-of-23-august-2021
dataset_id: rdls_hl-hti_unosat_damageassessmentchardonni_20210902
description: 'UNOSAT code: EQ20210814HTI This map illustrates potentially damaged
  structures/buildings in Chardonnieres commune, South department of Haiti as detected
  by Pleiades image acquired on 23 August 2021. Within the analyzed area, UNOSAT has
  identified 27 damaged structures, 107 potentially damaged structures, 9 landslide
  locations. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-chardonnieres-commune-south-department-as-of-23-august-2021]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts performed visual interpretation of Pleiades satellite
    imagery acquired 10 days post-earthquake, comparing pre- and post-event images
    to identify structural damage and secondary hazards. Damage was classified into
    confirmed damaged, potentially damaged, and undamaged categories with confidence
    levels. Landslide locations were also mapped as earthquake-triggered secondary
    impacts.
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
- href: https://data.humdata.org/dataset/damage-assessment-in-chardonnieres-commune-south-department-as-of-23-august-2021
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment identifying 27 confirmed damaged
      and 107 potentially damaged structures from earthquake ground shaking
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
  - asset_category: natural_environment
    asset_dimension: product
    description: Landslide locations (9 identified) triggered by earthquake ground
      motion
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
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
  description: Haiti - Damage Assessment in Chardonnieres commune, South department
    as of 23 August 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/HT/EQ20210814HTI/EQ20210814HTI_gdb.zip
  format: Geodatabase
  id: resource_b6d63630
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20210814HTI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Damage Assessment in Chardonnieres commune, South department
    as of 23 August 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/HT/EQ20210814HTI/EQ20210814HTI_shp.zip
  format: null
  id: resource_7e1375e8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20210814HTI_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-hti_unosat_damageassessmentchardonni_20210902
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-09-02'
temporal_resolution: null
title: Haiti - Damage Assessment in Chardonnieres commune, South department as of
  23 August 2021
version: null
vulnerability: null
---
