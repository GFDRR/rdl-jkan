---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Precipitation Measurement (GPM IMERG)
    url: https://data.humdata.org/dataset/accumulated-gpm-imerg-data-for-haiti-hurricane-matthew-october-3-6th-2016
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/accumulated-gpm-imerg-data-for-haiti-hurricane-matthew-october-3-6th-2016
creator:
  affiliation: null
  email: null
  name: Netherlands Red Cross - 510
  url: https://data.humdata.org/dataset/accumulated-gpm-imerg-data-for-haiti-hurricane-matthew-october-3-6th-2016
dataset_id: rdls_hzd-hti_nlrc510_accumulatedprecipitationh_20161013
description: 'Accumulated precipitation for Haiti - Hurricane Matthew - October 3-6th
  2016 Based on GPM IMERG data. See comments for assumptions and workflow.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/accumulated-gpm-imerg-data-for-haiti-hurricane-matthew-october-3-6th-2016]'
details: 'Data source: https://pmm.nasa.gov/data-access/downloads/gpm Admin areas:
  https://data.humdata.org/dataset/hti-polbndl-adm1-cnigs-zip Steps/assumptions: -
  the entire accumulated rainfall for 3, 4 and 5 october. (the data for 6 october
  indeed showed that the rain was gone). - I used the .tif/.twf files from the given
  source and used 3 of those combinations in total: 20161003 23.30-23.59-1day, 20161004
  23.30-23.59-1day and 20161005 23.30-23.59-1day. Since these respectively give the
  accumulated rainfall for 1 whole day ending at 23.59. - I used ''Zonal statistics''
  in QGIS to compute the average per administrative area and used the resulting ''mean''
  as output variable. Often, the administrative level 3 area was smaller than one
  raster point, but the resulting mean values seemed to reflect the average of the
  neighbouring raster point(s) when i inspected a few. - In the csv/xlsx I multiplied
  by 0.1, since the units in the data are in 0.1mm according to https://pps.gsfc.nasa.gov/Documents/README.GIS.pdf
  and the total amounts seemed to make sense like this (up to 700mm over 3 days in
  the worst hit areas, instead of 7000mm). The data output is similar to this video:
  https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=12389#59042 From this video you
  can also find the time frames in which Haiti incurred rain in relation to the typhoon.
  You can get GPM IMERG data here: https://pmm.nasa.gov/data-access/downloads/gpm.
  Note that IMERG tends to produce too much rainfall over land. We are working to
  address this problem in the next version of the algorithm, but unfortunately that
  won''t be until near the end of 2017. You can also look at an older algorithm from
  the TRMM Program: https://pmm.nasa.gov/data-access/downloads/trmm. That algorithm
  used to involve calibration using TRMM data, but TRMM ended in 2015, so now the
  algorithm uses a climatological calibration. For both algorithms, there is a real-time
  version and later science versions. The real-time versions use whatever data is
  available within a short time after the observation time. The science versions have
  longer latency, but use more data, including raingauge observations. The data sets
  come in a number of different formats listed on the pages. For the issues behind
  the over-estimation, I will refer you to the product developer, George Huffman,
  cc''d here. I don''t think it is a uniform over-estimation, but I don''t fully know
  the nature of the problem. Also, IMERG and TMPA have somewhat different estimates
  and deficiencies. In a conversation with George a moment ago, it sounded like the
  bigger issues were over the Southeastern U.S. rather than Haiti. In terms of latency,
  TMPA-RT (also known as 3B42-RT) has a real-time version available in about 8 hours
  after the observation time while the research product TMPA (3B42) has a latency
  of about 2 months. For IMERG, the real-time version is available in about 6 hours,
  a near-real-time-late product (with a bit more data) in 18 hours, and the final
  research version in about 4 months. These are near global products, so should work
  for just about any region except high latitudes. There are other rainfall products
  available elsewhere that attempt to do a similar type of analysis (such as NOAA''s
  CMORPH algorithm), but IMERG represents a combination of the best techniques in
  use by other products. IMERG is in the awkward position of having known flaws in
  the current version (3) and the new version (4) still being finalized. GPM hopes
  for a release by the end of November 2016. The current overestimation problem depends
  on the rain rate, when the rate goes above about 10 mm/hr, IMERG increasingly overestimates
  the rate. We picked up on this last October in South Carolina, USA, when the actual
  accumulations were in excess of 250 mm, but IMERG was high by a factor of two. Since
  then, we''ve seen other such examples. The real-time TMPA (product 3B42RT) doesn''t
  have this problem, but in fact the 3B42RT accumulations over land during Matthew
  were notably low (while IMERG Early or Late were notably high). A quick check over
  Haiti using Giovanni seems to show that (land and ocean both) 3B42RT is about 60%
  of IMERG-L, although, as you imply, it''s really hard to know what''s happening
  there. We compared the LATE to the EARLY GDM data and found first of all that the
  relative distribution over admin-areas does not change at all. second (see attached
  sheet) i find that the absolute amounts do not actually change that much (from a
  minimum factor 0.91 to a max of 1.24). what is weird is that on average the late
  rainfall is 5% higher than the early rainfall, which is the other way around from
  what the people at NASA expected. I can check with them if you like.'
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
      process: tornado
      trigger: null
      type: convective_storm
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: convective_storm
license: CC-BY-4.0
lineage:
  description: Accumulated precipitation data for Hurricane Matthew (October 3-6,
    2016) was derived from Global Precipitation Measurement (GPM) IMERG satellite
    observations and aggregated to Haiti administrative division 3 (commune) boundaries.
    The dataset represents observed rainfall measurements during the cyclone event
    without modeling or damage assessment.
  sources:
  - id: source_1
    license: null
    name: Global Precipitation Measurement (GPM IMERG)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/accumulated-gpm-imerg-data-for-haiti-hurricane-matthew-october-3-6th-2016
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Accumulated precipitation Hurricane Matthew (Excel)
  download_url: https://data.humdata.org/dataset/aa3cb121-cdec-459a-be82-23bdfa0e9149/resource/e1420f63-7b74-4e44-aa43-f03170689c4f/download/rainfall_adm3_oct3to5.xlsx
  format: null
  id: resource_e1420f63
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rainfall_adm3_oct3to5.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti - Accumulated precipitation Hurricane Matthew (PCODES, HXL)
  download_url: https://data.humdata.org/dataset/aa3cb121-cdec-459a-be82-23bdfa0e9149/resource/ebbc722b-0a42-41ec-8c25-0d9ec47e23ed/download/rainfall_adm3_oct3to5.xlsx
  format: null
  id: resource_ebbc722b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rainfall_adm3_oct3to5.xlsx
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hti_nlrc510_accumulatedprecipitationh_20161013
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-13'
temporal_resolution: null
title: Haiti - Accumulated precipitation Hurricane Matthew
version: null
vulnerability: null
---
