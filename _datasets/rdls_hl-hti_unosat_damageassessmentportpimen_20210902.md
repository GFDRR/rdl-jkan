---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-port-a-piment-and-coteaux-communes-south-department-as-of-23-august-2
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-port-a-piment-and-coteaux-communes-south-department-as-of-23-august-2
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-port-a-piment-and-coteaux-communes-south-department-as-of-23-august-2
dataset_id: rdls_hl-hti_unosat_damageassessmentportpimen_20210902
description: 'UNOSAT code: EQ20210814HTI This map illustrates potentially damaged
  structures/buildings in Port-A-Piment and Coteaux Communes, South department of
  Haiti as detected by Pleiades image acquired on 23 August 2021. Within the analyzed
  area, UNOSAT has identified 41 damaged structures, 72 potentially damaged structures,
  5 road obstacles, and 47 landslide locations. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to the United
  Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-port-a-piment-and-coteaux-communes-south-department-as-of-23-august-2]'
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
  description: UNOSAT analysts reviewed Pleiades satellite imagery acquired on 23
    August 2021 (9 days post-earthquake) and compared it with reference imagery to
    identify structural damage, road obstacles, and landslide locations in Port-A-Piment
    and Coteaux communes. The analysis is preliminary and field validation was pending
    at the time of publication.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-port-a-piment-and-coteaux-communes-south-department-as-of-23-august-2
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: 'Direct building damage from earthquake: 41 confirmed damaged and
      72 potentially damaged structures'
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: 'Infrastructure impact from earthquake: 5 road obstacles identified'
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: 'Secondary landslide hazard triggered by earthquake: 47 landslide
      locations identified'
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_3
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
  description: Haiti - Damage Assessment in Port-A-Piment and Coteaux communes, South
    department as of 23 August 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/HT/EQ20210814HTI/EQ20210814HTI_gdb.zip
  format: Geodatabase
  id: resource_f98b3128
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
  description: Haiti - Damage Assessment in Port-A-Piment and Coteaux communes, South
    department as of 23 August 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/HT/EQ20210814HTI/EQ20210814HTI_shp.zip
  format: null
  id: resource_77502a37
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
slug: rdls_hl-hti_unosat_damageassessmentportpimen_20210902
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
title: Haiti - Damage Assessment in Port-A-Piment and Coteaux communes, South department
  as of 23 August 2021
version: null
vulnerability: null
---
