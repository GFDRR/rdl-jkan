---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-jowhar-district-middle-shabelle-region-soma
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-jowhar-district-middle-shabelle-region-soma
dataset_id: rdls_hel-som_unosat_preliminaryderivedfloodas_20231109
description: 'UNOSAT code FL20231105SOM Status: Affected structures and inundated
  roads Further action(s): continue monitoring Inundated agricultural areas observed
  along the Shabelle River as of 08 November 2023; Affected structures observed in
  Jowhar City, Jowhar District, Middle Shabelle Region as of 08 November 2023; Potentially
  affected structures observed in Moyka Village, Jowhar District, Middle Shabelle
  Region as of 08 November 2023. Inundated roads observed in Jowhar City and Moyka
  Village, Jowhar District, Middle Shabelle Region as of 08 November 2023.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-jowhar-district-middle-shabelle-region-soma]'
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
    description: Affected and potentially affected structures in Jowhar City and Moyka
      Village
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
    description: Inundated road network in Jowhar City and Moyka Village
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
      quantity_kind: length
      unit: null
- asset_type:
    description: Inundated agricultural areas along the Shabelle River
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_3
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts manually reviewed and compared satellite imagery from
    8-9 November 2023 to identify post-flood impacts including affected structures,
    inundated roads, and flooded agricultural areas in Jowhar District. Vector geometries
    were digitized and attributed with sensor metadata, observation dates, and impact
    classifications to produce a rapid damage assessment product.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-jowhar-district-middle-shabelle-region-soma
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Affected structures identified in Jowhar City from fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
    description: Inundated roads in Jowhar City and Moyka Village from fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  - asset_category: agriculture
    asset_dimension: product
    description: Inundated agricultural areas along Shabelle River from fluvial flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
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
  description: Preliminary satellite-derived flood assessment - Jowhar District, Middle
    Shabelle Region, Somalia - 09 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3731/FL20231105SOM_gdb.zip
  format: Geodatabase
  id: resource_52b836d8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary satellite-derived flood assessment - Jowhar District, Middle
    Shabelle Region, Somalia - 09 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3731/FL20231105SOM_SHP.zip
  format: null
  id: resource_89b5bccf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-som_unosat_preliminaryderivedfloodas_20231109
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-09'
temporal_resolution: null
title: Preliminary satellite-derived flood assessment - Jowhar District, Middle Shabelle
  Region, Somalia - 09 November 2023
version: null
vulnerability: null
---
