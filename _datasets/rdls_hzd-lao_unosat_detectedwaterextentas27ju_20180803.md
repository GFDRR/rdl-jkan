---
attributions:
- entity:
    affiliation: null
    email: null
    name: Centro Internazionale In Monitoraggio Ambientale Research (CIMA)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Luxembourg Institute of Science and Technology (LIST)
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-
dataset_id: rdls_hzd-lao_unosat_detectedwaterextentas27ju_20180803
description: 'This map illustrates the satellite-detected surface waters extent in
  Sanamxay district, Attapeu province, as observed from the TerraSar-X and Tandem-X
  radar imagery acquired on 27 July 2018. Satellite detected water extent analysis
  was performed by Centro Internazionale In Monitoraggio Ambientale Research (CIMA)
  & Luxembourg Institute of Science and Technology (LIST). Within the analyzed area,
  a total of 7,405 ha were detected as inundated, four days after the collapse of
  the dam. Disclaimer: Flood extent maps are derived from high quality satellite data
  using a scientifically validated retrieval algorithm. No liability concerning the
  contents or the use thereof is assumed by the producer. The information has limitations
  due to the quality and resolution of the original data sources, as well as the uncertainties
  associated with the retrieval algorithm. Please be aware that the thematic accuracy
  might be lower in urban and forested areas due to inherent limitations of the SAR
  analysis technique. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-as-]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: TerraSar-X and Tandem-X radar satellite imagery acquired on 27 July
    2018 was analyzed by CIMA and LIST using scientifically validated change detection
    methods. UNOSAT analysts compared satellite images to identify surface water extent
    changes following the dam collapse, resulting in a vector polygon dataset of 7,405
    ha of inundated area with confidence and validation metadata.
  sources:
  - id: source_1
    license: null
    name: Centro Internazionale In Monitoraggio Ambientale Research (CIMA)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Luxembourg Institute of Science and Technology (LIST)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_3
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-as-
  rel: source
loss: null
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
  description: Satellite detected water extent as of 27 July 2018 over Sanamxay District,
    Attapeu Province, Lao PDR (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/LA/FL20180723LAO/FL20180723LAO_shp.zip
  format: null
  id: resource_46a80f0d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20180723LAO_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lao_unosat_detectedwaterextentas27ju_20180803
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-08-03'
temporal_resolution: null
title: Satellite detected water extent as of 27 July 2018 over Sanamxay District,
  Attapeu Province, Lao PDR
version: null
vulnerability: null
---
