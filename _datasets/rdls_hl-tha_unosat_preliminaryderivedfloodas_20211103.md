---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-central-and-western-part-of-thailand
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-central-and-western-part-of-thailand
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-central-and-western-part-of-thailand
dataset_id: rdls_hl-tha_unosat_preliminaryderivedfloodas_20211103
description: 'UNOSAT code: FL20210928THA Summary Of Findings; Floodwaters observed
  in 17 provinces as of 2 November 2021; Receding flood waters observed in Central
  Region as of 2 November 2021; Standing flood waters observed in Sukhothai, Phitsanulok,
  Kamphaeng Phet, Phichit, Phetchabun, Nakhon Sawan, Uthai Thani, and Kanchanaburi
  provinces as of 2 November 2021; Increased standing flood waters observed in Chai
  Nat, Suphan Buri, Sing Buri, Ang Thong, Saraburi, Lop Buri, Ayutthaya, Nakhon Pathom
  and Pathum Thani provinces as of 2 November 2021.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-central-and-western-part-of-thailand]'
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery to identify
    notable changes in water extent between pre- and post-flood scenes. Flood extent
    polygons were manually delineated and attributed with sensor date, area measurements,
    and qualitative observations of water status (standing vs. receding) across 17
    provinces in central and western Thailand as of November 2, 2021.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-central-and-western-part-of-thailand
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Flood extent and standing water observations across 17 affected provinces
      in central and western Thailand
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
  description: Preliminary Satellite-Derived Flood Assessment, Central and Western
    Part of Thailand (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TH/FL20210928THA/FL20210928THA_gdb.zip
  format: Geodatabase
  id: resource_e211acb4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210928THA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary Satellite-Derived Flood Assessment, Central and Western
    Part of Thailand (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TH/FL20210928THA/FL20210928THA_SHP.zip
  format: null
  id: resource_646becc1
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210928THA_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-tha_unosat_preliminaryderivedfloodas_20211103
spatial:
  bbox: null
  centroid: null
  countries:
  - THA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-11-03'
temporal_resolution: null
title: Preliminary Satellite-Derived Flood Assessment, Central and Western Part of
  Thailand
version: null
vulnerability: null
---
