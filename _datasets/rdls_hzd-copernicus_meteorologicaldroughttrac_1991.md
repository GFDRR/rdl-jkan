---
attributions:
- entity:
    affiliation: null
    email: null
    name: ERA5 fifth generation reanalysis
    url: https://data.humdata.org/dataset/global-meteorological-drought-tracking
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/global-meteorological-drought-tracking
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/global-meteorological-drought-tracking
dataset_id: rdls_hzd-copernicus_meteorologicaldroughttrac_1991
description: 'The Indicator for Meteorological Drought Tracking provides a clear spatio-temporal
  identification of persistent low-precipitation conditions at the global scale and
  at near real-time. It provides the outline and the duration and total spatial extent
  of drought clusters. The indicator is based on the Standardized Precipitation Index
  (SPI) for 3-months accumulation periods (i.e. SPI-3). The SPI indicator is derived
  from the ERA5 fifth generation reanalysis for the global climate and weather of
  the ECMWF, with baseline 1991-2020. Drought events are identified by means of a
  three dimensional density-based clustering algorithm (DBSCAN).. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/global-meteorological-drought-tracking]'
details: A range of different degrees of clustering can be obtained using different
  model settings and parameterization, meaning that a same parameterization at the
  global scale can likely result in overestimation/underestimation of drought events
  in certain areas.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Standardized Precipitation Index (SPI-3) is calculated from ERA5 global
    reanalysis precipitation data with a 1991-2020 baseline. Drought events are identified
    through three-dimensional clustering analysis to delineate persistent low-precipitation
    conditions, with spatial extent and duration tracked at monthly intervals across
    the globe.
  sources:
  - id: source_1
    license: null
    name: ERA5 fifth generation reanalysis
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/global-meteorological-drought-tracking
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
  url: https://drought.emergency.copernicus.eu/data/factsheets/factsheet_met_drought_tracking.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2025-01-01
    to 2025-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/a4426b7f-dc16-48b8-9d1e-5c90ec3e4217/download/jspa3_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_a4426b7f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2024-01-01
    to 2024-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/b96ae75f-3586-4d5e-9835-de2f686f49f0/download/jspa3_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_b96ae75f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2023-01-01
    to 2023-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/21c677e4-adcb-46e6-8cb7-3cd7712478b4/download/jspa3_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_21c677e4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2022-01-01
    to 2022-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/c32848ca-e1e3-4e4b-8d15-c0ab0fbb5b90/download/jspa3_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_c32848ca
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2021-01-01
    to 2021-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/ce8f6bb1-c5e6-482a-8bed-b6467f4b4f7b/download/jspa3_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_ce8f6bb1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2020-01-01
    to 2020-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/8f79cab6-ea1a-4a27-b7c8-7577d4f7bf2e/download/jspa3_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_8f79cab6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2019-01-01
    to 2019-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/34374b41-fc85-40b2-b83f-be2a6df0edc3/download/jspa3_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_34374b41
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2018-01-01
    to 2018-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/5d3bff8e-85f0-42dd-8bcd-d4ee6e174006/download/jspa3_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_5d3bff8e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2017-01-01
    to 2017-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/4aa61717-a386-4c13-9528-0a8ffaba4489/download/jspa3_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_4aa61717
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2016-01-01
    to 2016-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/acc6a29b-412c-442d-83b2-88ec4b089ed2/download/jspa3_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_acc6a29b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2015-01-01
    to 2015-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/9d1f5153-c46f-4a9e-b742-1e1492bab22c/download/jspa3_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_9d1f5153
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2014-01-01
    to 2014-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/242e1b61-083a-4fe5-934d-beadd7cb739c/download/jspa3_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_242e1b61
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2013-01-01
    to 2013-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/6ebdfa05-7c31-4610-9573-7b13f3391e97/download/jspa3_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_6ebdfa05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2012-01-01
    to 2012-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/7b30bc4e-60de-43cf-a8f3-dcfb9163c55d/download/jspa3_m_gdo_20120101_20121221_t.zip
  format: null
  id: resource_7b30bc4e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20120101_20121221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2011-01-01
    to 2011-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/bf3764c7-9a63-467d-b455-edac3aad91a7/download/jspa3_m_gdo_20110101_20111221_t.zip
  format: null
  id: resource_bf3764c7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20110101_20111221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2010-01-01
    to 2010-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/971331bc-30ab-4777-9485-568fdb2c5933/download/jspa3_m_gdo_20100101_20101221_t.zip
  format: null
  id: resource_971331bc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20100101_20101221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2009-01-01
    to 2009-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/e7d5ab78-9f5b-4cd0-8bc2-13af20e77f7b/download/jspa3_m_gdo_20090101_20091221_t.zip
  format: null
  id: resource_e7d5ab78
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20090101_20091221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2008-01-01
    to 2008-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/3dd66337-7889-48ff-96a6-c08ad71b9bc7/download/jspa3_m_gdo_20080101_20081221_t.zip
  format: null
  id: resource_3dd66337
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20080101_20081221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2007-01-01
    to 2007-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/429a98db-ebc1-4e6d-9d54-54954d065a5e/download/jspa3_m_gdo_20070101_20071221_t.zip
  format: null
  id: resource_429a98db
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20070101_20071221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2006-01-01
    to 2006-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/1a615791-2a99-4230-91f7-a362dd3ffb8e/download/jspa3_m_gdo_20060101_20061221_t.zip
  format: null
  id: resource_1a615791
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20060101_20061221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2005-01-01
    to 2005-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/f2212a15-0518-40cc-a57d-471a5f43993f/download/jspa3_m_gdo_20050101_20051221_t.zip
  format: null
  id: resource_f2212a15
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20050101_20051221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2004-01-01
    to 2004-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/6dfb3c8b-e35a-49c0-9329-056b9d9ce158/download/jspa3_m_gdo_20040101_20041221_t.zip
  format: null
  id: resource_6dfb3c8b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20040101_20041221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2003-01-01
    to 2003-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/57028eb9-b21a-49f0-ad83-1a68da4b73f0/download/jspa3_m_gdo_20030101_20031221_t.zip
  format: null
  id: resource_57028eb9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20030101_20031221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2002-01-01
    to 2002-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/5083739e-e261-416e-a8e0-a204fcab4fa0/download/jspa3_m_gdo_20020101_20021221_t.zip
  format: null
  id: resource_5083739e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20020101_20021221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2001-01-01
    to 2001-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/8c1d4ba2-06aa-45e9-b494-c4906bd1f901/download/jspa3_m_gdo_20010101_20011221_t.zip
  format: null
  id: resource_8c1d4ba2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20010101_20011221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 2000-01-01
    to 2000-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/8177862d-f37f-40e9-a4d5-76a2142481e6/download/jspa3_m_gdo_20000101_20001221_t.zip
  format: null
  id: resource_8177862d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_20000101_20001221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1999-01-01
    to 1999-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/146e0de8-4fa0-4426-9302-62930a482fc8/download/jspa3_m_gdo_19990101_19991221_t.zip
  format: null
  id: resource_146e0de8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19990101_19991221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1998-01-01
    to 1998-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/65d6e5c2-d403-49f7-9745-d6f8e0b22410/download/jspa3_m_gdo_19980101_19981221_t.zip
  format: null
  id: resource_65d6e5c2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19980101_19981221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1997-01-01
    to 1997-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/0ac466b3-bade-4a9e-bd50-6bb9c2534db9/download/jspa3_m_gdo_19970101_19971221_t.zip
  format: null
  id: resource_0ac466b3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19970101_19971221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1996-01-01
    to 1996-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/cf9acdd9-a3a5-44c9-b338-fbc01bafdceb/download/jspa3_m_gdo_19960101_19961221_t.zip
  format: null
  id: resource_cf9acdd9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19960101_19961221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1995-01-01
    to 1995-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/6cee2beb-de86-430c-af7e-6c97a31f6d8a/download/jspa3_m_gdo_19950101_19951221_t.zip
  format: null
  id: resource_6cee2beb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19950101_19951221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1994-01-01
    to 1994-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/b3f48823-a24f-40fe-b805-50b57dc3a759/download/jspa3_m_gdo_19940101_19941221_t.zip
  format: null
  id: resource_b3f48823
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19940101_19941221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1993-01-01
    to 1993-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/df58485a-b107-4a9c-99cc-4e3af5aa35be/download/jspa3_m_gdo_19930101_19931221_t.zip
  format: null
  id: resource_df58485a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19930101_19931221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1992-01-01
    to 1992-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/9a01b1b4-f90a-4263-a24f-98db6318bfe0/download/jspa3_m_gdo_19920101_19921221_t.zip
  format: null
  id: resource_9a01b1b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19920101_19921221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Copernicus Meteorological Drought Tracking (ERA5) (Data from 1991-02-11
    to 1991-12-31)
  download_url: https://data.humdata.org/dataset/4efff3a9-6449-4892-8fa4-d76f7374fa51/resource/a6744071-b745-4bda-86e7-776643121d2a/download/jspa3_m_gdo_19910211_19911221_t.zip
  format: null
  id: resource_a6744071
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jspa3_m_gdo_19910211_19911221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-copernicus_meteorologicaldroughttrac_1991
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '1991-02-11'
temporal_resolution: null
title: Copernicus Meteorological Drought Tracking (ERA5)
version: null
vulnerability: null
---
