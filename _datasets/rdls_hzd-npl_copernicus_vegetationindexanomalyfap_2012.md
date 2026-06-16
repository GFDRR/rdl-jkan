---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/npl-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/npl-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/npl-anomalies-fapar-viirs
dataset_id: rdls_hzd-npl_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/npl-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FAPAR:-
        process: agricultural_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values from VIIRS satellite observations are collected at 10-day
    intervals and processed into raster composites. Anomalies are calculated by computing
    the deviation of each grid cell's FAPAR value from its long-term mean baseline
    (2012 to the last available full year), enabling detection and monitoring of agricultural
    drought impacts on vegetation productivity across Nepal.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/npl-anomalies-fapar-viirs
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
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://drought.emergency.copernicus.eu/data/factsheets/factsheet_fapar_viirs.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/fdd3b952-86be-4e26-960e-1186ab90e204/download/npl_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_fdd3b952
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/b93bbb70-dab2-43b9-93dc-ee3efc4ca343/download/npl_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_b93bbb70
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/228c9ce5-dcb0-4a98-a91a-0ee77af2b438/download/npl_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_228c9ce5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/d47d1334-050c-48b7-a1f1-e5a45778e899/download/npl_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_d47d1334
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/46d76eaa-9cac-4100-a8af-10f70642e6f3/download/npl_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_46d76eaa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/96fc9170-d6cf-434a-9c8e-005fdbdd075b/download/npl_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_96fc9170
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/220bb7a6-1f1c-4517-a490-9370b92cb0db/download/npl_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_220bb7a6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/ff1cc1ad-c96b-41c2-b477-a8c0a29ab276/download/npl_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_ff1cc1ad
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/28fc3154-a8f8-4dfb-8d8f-de07b74ab9d0/download/npl_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_28fc3154
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/8d7f8f43-fc47-41b9-bec9-c4bb62bb416e/download/npl_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_8d7f8f43
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/513aa236-70c3-4cc5-9999-5ae990b133b4/download/npl_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_513aa236
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/378ef129-d6ab-4b38-85b8-05de28e760d2/download/npl_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_378ef129
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/2f00ef09-4e64-47ab-8ca3-29dc338853e0/download/npl_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_2f00ef09
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/bce25cf3-cf5d-484f-81b8-d1dca3a49adf/download/npl_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_bce25cf3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/fd80e4df-cb81-445f-80bf-56a96ae80103/resource/98175710-b1b2-4832-911d-9d3a07c9b0f4/download/npl_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_98175710
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: npl_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-npl_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Nepal: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
