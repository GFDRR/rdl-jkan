---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-impact-analysis-in-kalehe-territory-sud-kivu-province-democratic-republic-of-the
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-kalehe-territory-sud-kivu-province-democratic-republic-of-the
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-impact-analysis-in-kalehe-territory-sud-kivu-province-democratic-republic-of-the
dataset_id: rdls_hl-cod_unosat_landslideimpactanalysiska_20230509
description: 'UNOSAT code FL20230508COD, GDACS Id: 1101981 This map illustrates satellite-detected
  landslides/mudflow-related impact in Kalehe Territory, Sud-Kivu Province, Democratic
  Republic of the Congo as observed from a Sentinel-2 image acquired on 7 May 2023.
  Within the analysed area of about 9,000 ha, 90 ha of landslide scars were observed.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/landslide-impact-analysis-in-kalehe-territory-sud-kivu-province-democratic-republic-of-the]'
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
      intensity_measure: LSI:-
      process: landslide_mudflow
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts interpreted Sentinel-2 satellite imagery acquired on
    7 May 2023 over Kalehe Territory, comparing multi-temporal images to identify
    notable changes and detect landslide scars and mudflow features. The analysis
    identified 90 hectares of landslide impacts within a 9,000 hectare study area
    and produced vector geodatabase and shapefile outputs with spatial extent and
    area measurements.
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
- href: https://data.humdata.org/dataset/landslide-impact-analysis-in-kalehe-territory-sud-kivu-province-democratic-republic-of-the
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Land area affected by landslide scars and mudflow impacts
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
  description: Landslide impact analysis in Kalehe Territory, Sud-Kivu Province, Democratic
    Republic of the Congo as of 7 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3582/FL20230508COD_gdb.zip
  format: Geodatabase
  id: resource_67a2f997
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230508COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Landslide impact analysis in Kalehe Territory, Sud-Kivu Province, Democratic
    Republic of the Congo as of 7 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3582/FL20230508COD_SHP.zip
  format: null
  id: resource_78144f39
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230508COD_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-cod_unosat_landslideimpactanalysiska_20230509
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-09'
temporal_resolution: null
title: Landslide impact analysis in Kalehe Territory, Sud-Kivu Province, Democratic
  Republic of the Congo as of 7 May 2023
version: null
vulnerability: null
---
