---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-lower-northeastern-part-of-thailand-as-o
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-lower-northeastern-part-of-thailand-as-o
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-lower-northeastern-part-of-thailand-as-o
dataset_id: rdls_hl-tha_unosat_preliminaryderivedfloodas_20211112
description: 'UNOSAT code: FL20210928THA Summary of finding - Floodwaters observed
  in 13 provinces as of 11 November 2021; - Receding floodwaters observed in Lower
  Northeastern Region as of 11 November 2021; - Receding floodwaters observed in Amnat
  Chareon, Buri Ram, Chaiyaphum, Khon Kaen, and Nakhon Ratchasima provinces as of
  11 November 2021; - Floodwaters increase observed in Kalasin, Maha Sarakham, Nong
  Bua Lam Phu, Roi Et, Si Sa Ket, Surin, Ubon Ratchathani, and Yasothon provinces
  as of 11 November 2021.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-lower-northeastern-part-of-thailand-as-o]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared multi-temporal satellite imagery to identify
    and map floodwater extent across Lower Northeastern Thailand as of 11 November
    2021. Observed changes between satellite scenes were used to delineate inundated
    areas and classify provinces by flood status (receding vs. increasing). Results
    are provided as vector geometries with area measurements in hectares and square
    meters.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-in-lower-northeastern-part-of-thailand-as-o
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Floodwater extent observed across 13 provinces with spatial delineation
      of inundated areas
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
  description: Preliminary satellite-derived flood assessment in Lower Northeastern
    Part of Thailand as of 11 November 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TH/FL20210928THA/FL20210928THA_gdb.zip
  format: Geodatabase
  id: resource_564dac45
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
  description: Preliminary satellite-derived flood assessment in Lower Northeastern
    Part of Thailand as of 11 November 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TH/FL20210928THA/FL20210928THA_SHP.zip
  format: null
  id: resource_6f66129d
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
slug: rdls_hl-tha_unosat_preliminaryderivedfloodas_20211112
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
  start: '2021-11-12'
temporal_resolution: null
title: Preliminary satellite-derived flood assessment in Lower Northeastern Part of
  Thailand as of 11 November 2021
version: null
vulnerability: null
---
