---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-landslide-impact-assessment
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-landslide-impact-assessment
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-landslide-impact-assessment
dataset_id: rdls_lss-png_unosat_preliminaryderivedlandsli_20240530
description: 'UNOSAT code: LS20240525PNG, GDACS ID: 1102646 Status: Damaged structures
  observed Further action(s): Continue monitoring Damaged structures, roads and landslide
  area observed in Lagaip/Pogera District, Enga Province, Papua New Guinea as of 24
  May 2024.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-landslide-impact-assessment]'
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
  description: Satellite imagery acquired on or before 24 May 2024 was analyzed by
    UNOSAT analysts using visual interpretation and change detection techniques to
    identify damaged structures, roads, and the landslide extent in Lagaip/Pogera
    District, Enga Province, Papua New Guinea (GDACS event 1102646). Results were
    digitized into vector geodatabase and shapefile formats capturing site-level damage
    observations with confidence ratings and sensor metadata.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-landslide-impact-assessment
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-derived assessment of damaged structures observed in Lagaip/Pogera
      District, Enga Province, Papua New Guinea following a landslide event on 24
      May 2024
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
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
    description: Satellite-derived assessment of damaged roads observed in Lagaip/Pogera
      District, Enga Province, Papua New Guinea following a landslide event on 24
      May 2024
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
  description: Papua New Guinea - Preliminary satellite-derived landslide impact assessment
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3859/LS20240525PNG_gdb.zip
  format: Geodatabase
  id: resource_d41459c7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240525PNG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Papua New Guinea - Preliminary satellite-derived landslide impact assessment
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3859/LS20240525PNG_SHP.zip
  format: null
  id: resource_b724b1f8
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20240525PNG_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-png_unosat_preliminaryderivedlandsli_20240530
spatial:
  bbox: null
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-30'
temporal_resolution: null
title: Papua New Guinea - Preliminary satellite-derived landslide impact assessment
version: null
vulnerability: null
---
