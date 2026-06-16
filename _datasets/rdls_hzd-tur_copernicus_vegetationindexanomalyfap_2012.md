---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/tur-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/tur-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/tur-anomalies-fapar-viirs
dataset_id: rdls_hzd-tur_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/tur-anomalies-fapar-viirs]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "FAPAR values from VIIRS satellite observations are composited at 10-day\
    \ intervals. Anomalies are calculated at each grid cell as the deviation from\
    \ a long-term mean baseline (2012 to the last available full year), enabling detection\
    \ and monitoring of agricultural drought impacts on vegetation growth and productivity\
    \ across T\xFCrkiye."
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
- href: https://data.humdata.org/dataset/tur-anomalies-fapar-viirs
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
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2026-01-01 to 2026-01-10)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/f8eedef8-1bfd-417a-8956-726658e27859/download/tur_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_f8eedef8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2025-01-01 to 2025-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/a30ba4aa-4740-4bff-9ab1-eeff88544f0e/download/tur_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_a30ba4aa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2024-01-01 to 2024-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/0911c3d1-e2b7-4ad3-853f-8f050bfb9e83/download/tur_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_0911c3d1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2023-01-01 to 2023-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/c9a2e040-d90d-4ebf-95db-18ba35e0a63e/download/tur_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_c9a2e040
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2022-01-01 to 2022-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/898967f9-2568-4352-8818-e27de3949d13/download/tur_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_898967f9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2021-01-01 to 2021-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/6a6d3172-fe90-4755-8c5c-bbce61a70d43/download/tur_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_6a6d3172
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2020-01-01 to 2020-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/624c8054-b437-4c0a-a715-62997953ce49/download/tur_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_624c8054
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2019-01-01 to 2019-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/683feddc-c665-4dd0-b668-3a70716aad84/download/tur_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_683feddc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2018-01-01 to 2018-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/cded2a69-a805-44b2-b232-b4c7cdbabe20/download/tur_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_cded2a69
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2017-01-01 to 2017-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/980f4659-62a5-4177-9ab9-7a5c6f68e50d/download/tur_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_980f4659
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2016-01-01 to 2016-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/dda852f4-e9ef-4cf5-8cba-be65bb83520c/download/tur_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_dda852f4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2015-01-01 to 2015-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/3bc37b3e-86dc-46d8-a7fd-e242745eb668/download/tur_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_3bc37b3e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2014-01-01 to 2014-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/2de1a5ce-50df-4545-9884-873335de01e0/download/tur_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_2de1a5ce
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2013-01-01 to 2013-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/3f8cde76-04e8-4c31-aab3-3096dbd921ea/download/tur_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_3f8cde76
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2012-01-21 to 2012-12-31)"
  download_url: https://data.humdata.org/dataset/26980a16-261b-453f-84d8-42a6b4eb31c0/resource/1c9ae486-d7c3-41d2-a427-33052d00c91d/download/tur_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_1c9ae486
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tur_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-tur_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: "T\xFCrkiye: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)"
version: null
vulnerability: null
---
