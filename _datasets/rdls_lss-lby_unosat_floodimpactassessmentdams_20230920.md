---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-assessment-in-dams-over-benghazi-and-almarj-governorates-east-province-libya
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-dams-over-benghazi-and-almarj-governorates-east-province-libya
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-assessment-in-dams-over-benghazi-and-almarj-governorates-east-province-libya
dataset_id: rdls_lss-lby_unosat_floodimpactassessmentdams_20230920
description: 'UNOSAT code FL20230912LBY, GDACS Id: 1102204 This map illustrates satellite-detected
  flood impact in 4 dams over Benghazi and Almarj governorates, East pronvce, Libya,
  as observed from optical very-high resolution satellite imagery. Dam reservoirs
  appears to be filled over the 4 dams. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to the United Nations
  Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-assessment-in-dams-over-benghazi-and-almarj-governorates-east-province-libya]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared multi-temporal optical very-high resolution
    satellite imagery to detect flood impacts on 4 dams in Benghazi and Almarj governorates.
    Changes between images were identified to assess dam reservoir filling and inundation
    status. This is a preliminary post-event impact assessment not yet validated in
    the field.
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
- href: https://data.humdata.org/dataset/flood-impact-assessment-in-dams-over-benghazi-and-almarj-governorates-east-province-libya
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct impact to dam infrastructure from flood event, satellite-detected
      reservoir filling and inundation
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
  description: Flood impact assessment in Dams over Benghazi and Almarj Governorates,
    East Province, Libya (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3676/FL20230912LBY_gdb.zip
  format: Geodatabase
  id: resource_fee84d70
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact assessment in Dams over Benghazi and Almarj Governorates,
    East Province, Libya (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3676/FL20230912LBY_SHP.zip
  format: null
  id: resource_564eeea7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230912LBY_SHP.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-lby_unosat_floodimpactassessmentdams_20230920
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-20'
temporal_resolution: null
title: Flood impact assessment in Dams over Benghazi and Almarj Governorates, East
  Province, Libya
version: null
vulnerability: null
---
