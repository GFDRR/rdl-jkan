---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-region-dominican-republic-as-of-21-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-region-dominican-republic-as-of-21-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-region-dominican-republic-as-of-21-november-2023
dataset_id: rdls_he-dom_unosat_detectedwaterextentcibaon_20231122
description: "UNOSAT code: FL20231120DOM, GDACS ID: 1102342 This map illustrates cumulative\
  \ satellite-detected water extent in Cibao Nordeste Region, Dominican Republic as\
  \ observed from a Sentinel-2 image acquired on the 21 November 2023 at 11:17 local\
  \ time. Within the cloud free analysed area of about 920 km\xB2 , about 190 km\xB2\
  \ of land appears to be affected with flood waters and 13,000 people are potentially\
  \ exposed to flood waters. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-region-dominican-republic-as-of-21-november-2023]"
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
    description: Population potentially exposed to flood waters based on satellite-detected
      inundation extent
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-2 satellite image acquired on 21 November 2023 was analyzed\
    \ by UNOSAT through visual interpretation and multi-temporal comparison to detect\
    \ cumulative water extent changes. The resulting water extent polygon (190 km\xB2\
    \ within 920 km\xB2 cloud-free area) was vectorized and intersected with population\
    \ data to estimate exposure. This preliminary post-event damage assessment has\
    \ not been field-validated."
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
- href: https://data.humdata.org/dataset/water-extent-in-cibao-nordeste-region-dominican-republic-as-of-21-november-2023
  rel: source
loss:
  losses: []
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
  description: Satellite detected water extent in Cibao Nordeste Region, Dominican
    Republic as of 21 November 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3750/FL20231120DOM_gdb.zip
  format: Geodatabase
  id: resource_fbe0fdd4
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231120DOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Cibao Nordeste Region, Dominican
    Republic as of 21 November 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3750/FL20231120DOM_SHP.zip
  format: null
  id: resource_35686693
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231120DOM_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Cibao Nordeste Region, Dominican
    Republic as of 21 November 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3750/UNOSAT_Population_Exposure_FL20231120DOM_21Nov2023.xlsx
  format: null
  id: resource_85f52cad
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20231120DOM_21Nov2023.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-dom_unosat_detectedwaterextentcibaon_20231122
spatial:
  bbox: null
  centroid: null
  countries:
  - DOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-22'
temporal_resolution: null
title: Satellite detected water extent in Cibao Nordeste Region, Dominican Republic
  as of 21 November 2023
version: null
vulnerability: null
---
