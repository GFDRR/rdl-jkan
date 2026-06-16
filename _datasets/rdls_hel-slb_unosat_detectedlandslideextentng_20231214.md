---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-extent-in-the-nggela-constituency-central-province-solomon-island-as-of-14-decem
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-extent-in-the-nggela-constituency-central-province-solomon-island-as-of-14-decem
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-extent-in-the-nggela-constituency-central-province-solomon-island-as-of-14-decem
dataset_id: rdls_hel-slb_unosat_detectedlandslideextentng_20231214
description: 'UNOSAT code: TC20231206SLB, GDACS ID: 1001038 Satellite detected landslide
  extent in the Nggela Constituency, Central Province, Solomon Island as of 14 December
  2023 This map illustrates satellite-detected landslides in Nggela Constituency,
  Central Province, Solomon Islands, as observed from a Sentinel-2 satellite acquired
  on 14 December 2023 at 10:39 local time. Within the analyzed area of 400 ha about
  12 ha of landslide extent is observed. UNOSAT identified 7 potentially affected
  structures. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT)..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-extent-in-the-nggela-constituency-central-province-solomon-island-as-of-14-decem]'
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
    description: Potentially affected structures identified within the landslide extent
      area
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
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on 14
    December 2023 and compared it with reference imagery to identify notable changes
    indicative of landslide occurrence. Landslide polygons were manually delineated
    and attributed with area measurements and affected structure counts. This is a
    preliminary post-event damage assessment based on remote sensing observation without
    field validation.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/landslide-extent-in-the-nggela-constituency-central-province-solomon-island-as-of-14-decem
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Structures potentially affected by satellite-detected landslides
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
  description: Solomon Islands - Satellite detected landslide extent in the Nggela
    Constituency, Central Province, Solomon Island as of 14 December 2023 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3773/TC20231206SLB_gdb.zip
  format: Geodatabase
  id: resource_947108e9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20231206SLB_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Solomon Islands - Satellite detected landslide extent in the Nggela
    Constituency, Central Province, Solomon Island as of 14 December 2023 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3773/TC20231206SLB_SHP.zip
  format: null
  id: resource_d835023c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20231206SLB_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-slb_unosat_detectedlandslideextentng_20231214
spatial:
  bbox: null
  centroid: null
  countries:
  - SLB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-12-14'
temporal_resolution: null
title: Solomon Islands - Satellite detected landslide extent in the Nggela Constituency,
  Central Province, Solomon Island as of 14 December 2023
version: null
vulnerability: null
---
