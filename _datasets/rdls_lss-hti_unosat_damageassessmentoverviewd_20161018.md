---
attributions:
- entity:
    affiliation: null
    email: null
    name: UNITAR-UNOSAT
    url: https://data.humdata.org/dataset/damage-assessment-overview-of-dame-marie-and-anse-d-hainault-areas-grande-anse-sud-departments
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Copernicus Emergency Management Service
    url: https://data.humdata.org/dataset/damage-assessment-overview-of-dame-marie-and-anse-d-hainault-areas-grande-anse-sud-departments
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-overview-of-dame-marie-and-anse-d-hainault-areas-grande-anse-sud-departments
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-overview-of-dame-marie-and-anse-d-hainault-areas-grande-anse-sud-departments
dataset_id: rdls_lss-hti_unosat_damageassessmentoverviewd_20161018
description: 'This map illustrates potentially damaged satellite-detected areas, related
  damage density and the identified road obstacles in the southwestern part of Haiti
  in Grande Anse and Sud departments, Haiti. The UNITAR-UNOSAT analysis used a Pleiades
  satellite image acquired on the 12 October 2016. The UNITAR-UNOSAT analysis combined
  with Copernicus analysis, identified 9,173 potentially damaged structures within
  this map extent. Additionally, 123 road obstacles and 255 population gathering sites
  within this area were identified in the analysis. Please note that some areas were
  cloud covered and could not be analysed. This is a preliminary analysis and has
  not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-overview-of-dame-marie-and-anse-d-hainault-areas-grande-anse-sud-departments]'
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
  description: Post-event satellite imagery from Pleiades (acquired 12 October 2016)
    was analyzed by UNOSAT using change detection methods, comparing pre- and post-event
    imagery to identify potentially damaged structures, road obstacles, and population
    gathering sites in Grande Anse and Sud departments of Haiti following Hurricane
    Matthew (October 2016). The UNOSAT analysis was combined with Copernicus Emergency
    Management Service outputs to produce a unified geodatabase of impact features.
    The resulting dataset supports humanitarian response and damage assessment operations
    in the affected area.
  sources:
  - id: source_1
    license: null
    name: UNITAR-UNOSAT
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Copernicus Emergency Management Service
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-overview-of-dame-marie-and-anse-d-hainault-areas-grande-anse-sud-departments
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-detected potentially damaged structures (9,173) in Grande
      Anse and Sud departments following Hurricane Matthew, derived from Pleiades
      imagery analysis by UNOSAT and Copernicus
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
    description: Road obstacles (123) identified in the affected area following Hurricane
      Matthew, detected via satellite imagery change detection
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
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population gathering sites (255) identified in the affected area,
      indicating displaced or congregating populations following Hurricane Matthew
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
    id: loss_3
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
  description: Haiti - Damage Assessment Overview of Dame Marie and Anse d'Hainault
    Areas, Grande Anse & Sud Departments (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_gdb.zip
  format: Geodatabase
  id: resource_78b4304d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Damage Assessment Overview of Dame Marie and Anse d'Hainault
    Areas, Grande Anse & Sud Departments (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/HT/TC20161003HTI/TC20161003THI_combined_shp.zip
  format: null
  id: resource_3a7bd133
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20161003THI_combined_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_unosat_damageassessmentoverviewd_20161018
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
  start: '2016-10-18'
temporal_resolution: null
title: Haiti - Damage Assessment Overview of Dame Marie and Anse d'Hainault Areas,
  Grande Anse & Sud Departments
version: null
vulnerability: null
---
