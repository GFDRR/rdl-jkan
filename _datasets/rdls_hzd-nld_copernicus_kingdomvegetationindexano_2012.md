---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/nld-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/nld-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/nld-anomalies-fapar-viirs
dataset_id: rdls_hzd-nld_copernicus_kingdomvegetationindexano_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/nld-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
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
      intensity_measure: FAPAR:-
      process: agricultural_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals. Anomalies are calculated at each grid cell as the deviation from a
    long-term mean baseline (2012 to last available full year), generating raster
    datasets to monitor agricultural drought impacts on vegetation productivity across
    the Netherlands.
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
- href: https://data.humdata.org/dataset/nld-anomalies-fapar-viirs
  rel: source
loss: null
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
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/7722f95c-38c5-45f3-9f3e-1c13528d17aa/download/nld_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_7722f95c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/74ec03ef-0c48-477a-8c51-41141badd457/download/nld_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_74ec03ef
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/3b16bbb6-67e1-4954-a589-eef3c1d9d9c5/download/nld_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_3b16bbb6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/a7b8fb62-7033-4fff-9ff0-8b142ab2a7fb/download/nld_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_a7b8fb62
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/dda957ca-0426-4cb4-9b0a-a0b3bd20eb6c/download/nld_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_dda957ca
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/b2055a4b-19e8-469e-9298-86ef535aae90/download/nld_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_b2055a4b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/f4d5406b-96ca-4133-83d0-1df1d343527c/download/nld_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_f4d5406b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/afa6ce86-2b04-438a-8706-f9bfab56f860/download/nld_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_afa6ce86
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/745baf0e-d2fc-4cb9-8039-7fa55c48fcc7/download/nld_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_745baf0e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/b62c2f5a-0d16-462c-9f56-617a9012ddc7/download/nld_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_b62c2f5a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/65a34342-aa64-45c7-82c2-82ed1c5ec4c0/download/nld_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_65a34342
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/173638f9-7d66-4abc-8176-b60b6b9782c7/download/nld_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_173638f9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/252baee8-6a9b-42fb-9af3-d6cfa4f6b88b/download/nld_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_252baee8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/6ae74895-f371-42b5-84b9-69c61bed703b/download/nld_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_6ae74895
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/d90d229c-ce63-4622-9072-8ac6904b47a2/resource/9a9d284a-5dae-413e-a3d1-735a0d69d0b2/download/nld_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_9a9d284a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-nld_copernicus_kingdomvegetationindexano_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - NLD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Netherlands (Kingdom of the): Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
