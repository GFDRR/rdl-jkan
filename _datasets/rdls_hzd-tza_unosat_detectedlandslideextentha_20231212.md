---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/landslide-extent-in-hanang-district-manyara-region-tanzania-as-of-07-december-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-extent-in-hanang-district-manyara-region-tanzania-as-of-07-december-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/landslide-extent-in-hanang-district-manyara-region-tanzania-as-of-07-december-2023
dataset_id: rdls_hzd-tza_unosat_detectedlandslideextentha_20231212
description: 'UNOSAT code: LS20231208TZA This map illustrates satellite detected landslides
  in Hanang District, Manyara Region, Tanzania as observed from a Sentinel-2 acquired
  on 07 December 2023 at 11:11 local time. Within the analyzed area of 4,000 ha, about
  75 ha of landslides scars are observed. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to the United Nations
  Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/landslide-extent-in-hanang-district-manyara-region-tanzania-as-of-07-december-2023]'
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
  event_sets_by_hazard_type:
    landslide:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-2 satellite imagery acquired on 7 December 2023 was analyzed
    by UNOSAT through manual visual interpretation and comparison with reference imagery
    to detect and delineate landslide scars. Landslide polygons were digitized and
    attributed with area measurements (75 ha total within 4,000 ha study area). This
    is a preliminary post-event observation dataset not yet validated through field
    surveys.
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
- href: https://data.humdata.org/dataset/landslide-extent-in-hanang-district-manyara-region-tanzania-as-of-07-december-2023
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
  description: Satellite detected landslide extent in Hanang District, Manyara Region,
    Tanzania as of 07 December 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3768/LS20231208TZA_gdb.zip
  format: Geodatabase
  id: resource_1b95dead
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20231208TZA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected landslide extent in Hanang District, Manyara Region,
    Tanzania as of 07 December 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3768/LS20231208TZA_SHP.zip
  format: null
  id: resource_c9a93810
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: LS20231208TZA_SHP.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-tza_unosat_detectedlandslideextentha_20231212
spatial:
  bbox: null
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-12-12'
temporal_resolution: null
title: Satellite detected landslide extent in Hanang District, Manyara Region, Tanzania
  as of 07 December 2023
version: null
vulnerability: null
---
