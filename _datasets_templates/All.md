---
schema: rdl
title:
category:
  - Hazard
  - Exposure
  - Vulnerability
  - Loss
notes:
organization:
source: SWIO RAFI
model_date:
version:
purpose:
project:
bibliography:
geo_coverage:
  - ABW
  - AFG
  - AGO
  - AIA
  - ALB
  - AND
  - ARE
  - ARG
  - ARM
  - ASM
  - ATG
  - AUS
  - AUT
  - AZE
  - BDI
  - BEL
  - BEN
  - BFA
  - BGD
  - BGR
  - BHR
  - BHS
  - BIH
  - BLM
  - BLR
  - BLZ
  - BMU
  - BOL
  - BRA
  - BRB
  - BRN
  - BTN
  - BWA
  - CAF
  - CAN
  - CHE
  - CHL
  - CHN
  - CIV
  - CMR
  - COD
  - COG
  - COK
  - COL
  - COM
  - CPV
  - CRI
  - CUB
  - CUW
  - CYM
  - CYP
  - CZE
  - DEU
  - DJI
  - DMA
  - DNK
  - DOM
  - DZA
  - ECU
  - EGY
  - ERI
  - ESP
  - EST
  - ETH
  - FIN
  - FJI
  - FLK
  - FRA
  - FRO
  - FSM
  - GAB
  - GBR
  - GEO
  - GGY
  - GHA
  - GIB
  - GIN
  - GMB
  - GNB
  - GNQ
  - GRC
  - GRD
  - GRL
  - GTM
  - GUM
  - GUY
  - HKG
  - HMD
  - HND
  - HRV
  - HTI
  - HUN
  - IDN
  - IMN
  - IND
  - IRL
  - IRN
  - IRQ
  - ISL
  - ISR
  - ITA
  - JAM
  - JEY
  - JOR
  - JPN
  - KAZ
  - KEN
  - KGZ
  - KHM
  - KIR
  - KNA
  - KOR
  - KWT
  - LAO
  - LBN
  - LBR
  - LBY
  - LCA
  - LIE
  - LKA
  - LSO
  - LTU
  - LUX
  - LVA
  - MAC
  - MAF
  - MAR
  - MCO
  - MDA
  - MDG
  - MDV
  - MEX
  - MHL
  - MKD
  - MLI
  - MLT
  - MMR
  - MNE
  - MNG
  - MNP
  - MOZ
  - MRT
  - MSR
  - MUS
  - MWI
  - MYS
  - NAM
  - NCL
  - NER
  - NFK
  - NGA
  - NIC
  - NIU
  - NLD
  - NOR
  - NPL
  - NRU
  - NZL
  - OMN
  - PAK
  - PAN
  - PCN
  - PER
  - PHL
  - PLW
  - PNG
  - POL
  - PRI
  - PRK
  - PRT
  - PRY
  - PSE
  - PYF
  - QAT
  - ROU
  - RUS
  - RWA
  - SAU
  - SDN
  - SEN
  - SGP
  - SGS
  - SHN
  - SLB
  - SLE
  - SLV
  - SMR
  - SOM
  - SPM
  - SRB
  - SSD
  - STP
  - SUR
  - SVK
  - SVN
  - SWE
  - SWZ
  - SXM
  - SYC
  - SYR
  - TCA
  - TCD
  - TGO
  - THA
  - TJK
  - TKM
  - TLS
  - TON
  - TTO
  - TUN
  - TUR
  - TUV
  - TZA
  - UGA
  - UKR
  - URY
  - USA
  - UZB
  - VAT
  - VCT
  - VEN
  - VGB
  - VIR
  - VNM
  - VUT
  - WLF
  - WSM
  - XXK
  - YEM
  - ZAF
  - ZMB
  - ZWE 

resources:
  - name: package name and format
    url: 'https://rdl-jkan-datasets.s3-ap-southeast-2.amazonaws.com/COMP/NAME'
    format: gpkg
  - name: Afghanistan all RPs Shapefile
    url: 'https://rdl-jkan-datasets.s3-ap-southeast-2.amazonaws.com/COMP/NAME'
    format: shp

license:
  - CC0
  - CC BY 4.0
  - CC BY-SA 4.0
  - ODbl
  - ODC-By
  - PDDL
  - field_name: maintainer
    label: Maintainer
    datajson: contactPoint.fn
  - field_name: maintainer_email
    label: Maintainer Email
    datajson: contactPoint.hasEmail
      - Hazard
      - Exposure
      - Vulnerability
      - Loss  


resource_fields:
  - field_name: name
    label: Resource Name
    datajson: distribution.title
  - field_name: url
    label: URL
    datajson: distribution.downloadURL

organization_fields:
  - field_name: title
    label: Title
  - field_name: description
    label: Description
  - field_name: logo
    label: Logo

category_fields:
  - field_name: name
    label: Name
  - field_name: logo
    label: Logo
  - field_name: logo_credit
    label: Logo Credit
  - field_name: featured
    label: Featured on Homepage
    form_template: form/checkbox.html

rdl_fields:
  # RDL-attributes: hazard fields
  ## Event Set
  - field_name: event_hazard_type
    label: Hazard type
    values:
      - CF
      - CS
      - DR
      - EQ
      - ET
      - FL
      - LS 
      - MH
      - TS
      - VO
      - WF
      - WI
  - field_name: geo_area_name
    label: Name of location covered (local-scale datasets)
  - field_name: event_time_start
    label: Event start time
  - field_name: event_time_end
    label: Event end time
  - field_name: event_time_duration
    label: Time duration
  - field_name: event_description
    label: Event description
  - field_name: event_is_prob
    label: Is prob
    values:
      - True
      - False

  ## Event
  - field_name: event_calculation_method
    label: Calculation method
  - field_name: event_frequency
    label: Frequency
  - field_name: event_occurence_probability
    label: Occurence probability
  - field_name: event_occurrence_time_start
    label: Occurrence time start
  - field_name: event_occurrence_time_end
    label: Occurrence time end
  - field_name: event_occurrence_time_span
    label: Occurrence time span
  - field_name: event_trigger_hazard_type
    label: Trigger hazard type
    values:
      - CF
      - CS
      - DR
      - EQ
      - ET
      - FL
      - LS 
      - MH
      - TS
      - VO
      - WF
      - WI
  - field_name: event_trigger_process_type
    label: Trigger Process Type
    values:
      - FCF
      - FSS
      - TOR
      - DTA
      - DTH
      - DTM
      - DTS
      - Q1R
      - Q2R
      - QGM
      - QLI
      - ECD
      - EHT
      - FFF
      - FPF
      - LAV
      - LSL
      - TSI
      - VAF
      - VBL
      - VFH
      - VLH
      - VLV
      - VPF
      - WFI
      - ETC
      - TCY
  - field_name: event_trigger_event
    label: Trigger event
  - field_name: event_description
    label: Description specific to this event

  ## FootprintSet
  - field_name: footprintset_process_type
    label: Process type
    values:
      - FCF
      - FSS
      - TOR
      - DTA
      - DTH
      - DTM
      - DTS
      - Q1R
      - Q2R
      - QGM
      - QLI
      - ECD
      - EHT
      - FFF
      - FPF
      - LAV
      - LSL
      - TSI
      - VAF
      - VBL
      - VFH
      - VLH
      - VLV
      - VPF
      - WFI
      - ETC
      - TCY
  - field_name: footprintset_IMT
    label: Intensity measure
    values:
      - PGA_g
      - PGA_m/s2
      - PGV_m/s
      - SA(0.2)_g
      - SA(0.3)_g
      - SA(1.0)_g
      - SA(3.0)_g
      - SA(0.2)_m/s2
      - SA(0.3)_m/s2
      - SA(1.0)_m/s2
      - SA(3.0)_m/s2
      - Sd(T1)_m
      - Sv(T1)_m/s
      - PGDf_m
      - D_a5-95_s
      - D_a5-75 _s
      - IA_m/s
      - Neq_-
      - EMS_-
      - AvgSa_m/s2
      - I_Np_m/s2
      - MMI_-
      - CAV_m/s
      - D_B_s
      - d_fff_m
      - d_fpf_m
      - v_fff_m/s
      - v_fpf_m/s
      - v_tcy(3s)_km/h
      - v_ect(3s)_km/h
      - v_tcy(1m)_km/h
      - v_ect(1m)_km/h
      - v_tcy(10m)_km/h
      - v_etc(10m)_km/h
      - PGWS_tcy_km/h
      - PGWS_ect_km/h
      - d_lsl_m
      - I_DF_m3/s2
      - v_lsl_m/s2
      - MFD_lsl_m
      - SD_lsl_m
      - LSI_-
      - haz_lsl_-
      - Rh_tsi_m
      - d_tsi_m
      - MMF_m4/s2
      - F_drag_kN
      - Fr_-
      - v_tsi_m/s
      - F_QS_kN
      - MF_m3/s2
      - h_tsi_m
      - Fh_tsi_m
      - h_vaf_m
      - L_vaf_kg/m2
      - v_fss_m/s
      - d_fss_m
      - CMI_-
      - PDSI_-
      - SPI_-
  - field_name: footprintset_data_uncertainty
    label: Data uncertainty

  ## Footprint
  - field_name: footprint_uncertainty_2nd_moment
    label: Uncertainty 2nd moment
  - field_name: footprint_trigger_footprint
    label: Trigger footprint

  ## Footprint Data
  ### Not needed for RDL-JKAN
  # file_location

  # RDL-Exposure fields
  ## ExposureModel
  - field_name: exposure_name
    label: Exposure Name
  - field_name: exposure_description
    label: Description
  - field_name: exposure_taxonomy_source
    label: Taxonomy source
  - field_name: exposure_category
    label: Exposure category
    values:
      - Buildings
      - Indicators
      - Infrastructures
      - Crops, livestock and forestry
  - field_name: exposure_area_type
    label: Area type
  - field_name: exposure_area_unit
    label: Area unit
  - field_name: exposure_tag_names
    label: Tag names
  - field_name: exposure_occupancy
    label: Occupancy
    values:
      - Residential
      - Commercial
      - Industrial
      - Infrastructure
      - Healthcare
      - Educational
      - Government
      - Crop
      - Livestock
      - Forestry
      - Mixed

  ## Asset
  - field_name: asset_ref
    label: Asset reference code
  - field_name: asset_taxonomy
    label: Taxonomy name
  - field_name: asset_number_of_units
    label: Number of units
  - field_name: asset_area
    label: Area

  ## CostType
  - field_name: cost_type_name
    label: Cost type name
  - field_name: cost_type_aggregation_type
    label: Aggregation type
  - field_name: cost_type_unit
    label: Cost unit of measure
      
  ## Cost and occupants are in-data values. Tags used for whole set specifications
  ### Not needed for RDL-JKAN
  # file_location

  ## Tags
  - field_name: tag_name
    label: Tag name
  - field_name: tag_value
    label: Tag value

  # RDL-Loss fields
  ## Model
  - field_name: model_name
    label: Model Name
  - field_name: model_description
    label: Model description
  - field_name: model_hazard_type
    label: Hazard Type
    values:
      - CF
      - CS
      - DR
      - EQ
      - ET
      - FL
      - LS 
      - MH
      - TS
      - VO
      - WF
      - WI
  - field_name: model_process_type
    label: Process Type
    values:
      - FCF
      - FSS
      - TOR
      - DTA
      - DTH
      - DTM
      - DTS
      - Q1R
      - Q2R
      - QGM
      - QLI
      - ECD
      - EHT
      - FFF
      - FPF
      - LAV
      - LSL
      - TSI
      - VAF
      - VBL
      - VFH
      - VLH
      - VLV
      - VPF
      - WFI
      - ETC
      - TCY
  - field_name: model_hazard_link
    label: Hazard Link
  - field_name: model_exposure_link
    label: Exposure Link
  - field_name: model_vulnerability_link
    label: Vulnerability Link
  
  ## Map
  - field_name: map_occupancy
    label: Occupancy
    values:
      - Residential
      - Commercial
      - Industrial
      - Infrastructure
      - Healthcare
      - Educational
      - Government
      - Crop
      - Livestock
      - Forestry
      - Mixed
  - field_name: map_category
    label: Category of exposed asset
    values:
      - Buildings
      - Indicators
      - Infrastructures
      - Crops, livestock and forestry     
  - field_name: map_element
    label: Element of loss
    values:
      - Structure
      - Content
      - Business interruption
      - Other
   - field_name: map_impact
    label: Impact type
    values:
      - Direct
      - Indirect
      - Mixed
  - field_name: map_loss_type
    label: Loss Type
    values:
      - Ground up
      - Insured
  - field_name: map_frequency
    label: Type of frequency
    values:
      - Rate of Exceedence
      - Probability of Exceedence
      - Return Period     
  - field_name: map_return_period
    label: Return Period in years
  - field_name: map_units
    label: Unit of measure
  - field_name: map_metric
    label: Metric
    values:
      - AAL
      - AALR
      - PML
  
  ## Map values
  ### Not needed for RDL-JKAN
  # file_location

  ## CurveMap
  - field_name: curve_map_occupancy
    label: Occupancy (Curve map)
    values:
      - Residential
      - Commercial
      - Industrial
      - Infrastructure
      - Healthcare
      - Educational
      - Government
      - Crop
      - Livestock
      - Forestry
      - Mixed
  - field_name: curve_map_category
    label: Category of exposed asset
    values:
      - Buildings
      - Indicators
      - Infrastructures
      - Crops, livestock and forestry     
  - field_name: curve_map_element
    label: Element of loss
    values:
      - Structure
      - Content
      - Business interruption
      - Other
   - field_name: curve_map_impact
    label: Impact type
    values:
      - Direct
      - Indirect
      - Mixed
  - field_name: curve_map_loss_type
    label: Loss Type
    values:
      - Ground up
      - Insured
  - field_name: curve_map_frequency
    label: Frequency representation type
  - field_name: curve_map_investigation_time
    label: Investigation Time
  - field_name: curve_map_units
    label: Unit of measure
  
  ## Curve map values
  ### Not needed for RDL-JKAN
  # file_location


  # RDL-Vulnerability fields
  ## Fcore
  - field_name: f_core_hazard_type_primary
    label: Primary hazard type
    values:
      - CF
      - CS
      - DR
      - EQ
      - ET
      - FL
      - LS 
      - MH
      - TS
      - VO
      - WF
      - WI
  - field_name: f_core_hazard_type_secondary
    label: Secondary hazard type
    values:
      - CF
      - CS
      - DR
      - EQ
      - ET
      - FL
      - LS 
      - MH
      - TS
      - VO
      - WF
      - WI
  - field_name: f_core_process_type_primary
    label: Primary process type
    values:
      - FCF
      - FSS
      - TOR
      - DTA
      - DTH
      - DTM
      - DTS
      - Q1R
      - Q2R
      - QGM
      - QLI
      - ECD
      - EHT
      - FFF
      - FPF
      - LAV
      - LSL
      - TSI
      - VAF
      - VBL
      - VFH
      - VLH
      - VLV
      - VPF
      - WFI
      - ETC
      - TCY
  - field_name: f_core_process_type_secondary
    label: Secondary process type
    values:
      - FCF
      - FSS
      - TOR
      - DTA
      - DTH
      - DTM
      - DTS
      - Q1R
      - Q2R
      - QGM
      - QLI
      - ECD
      - EHT
      - FFF
      - FPF
      - LAV
      - LSL
      - TSI
      - VAF
      - VBL
      - VFH
      - VLH
      - VLV
      - VPF
      - WFI
      - ETC
      - TCY
  - field_name: f_core_occupancy
    label: Occupancy
    values:
      - Residential
      - Commercial
      - Industrial
      - Infrastructure
      - Healthcare
      - Educational
      - Government
      - Crop
      - Livestock
      - Forestry
      - Mixed
  - field_name: f_core_taxonomy_source
    label: Taxonomy source
  - field_name: f_core_taxonomy
    label: Taxonomy
  - field_name: f_core_asset_type
    label: Asset type
  - field_name: f_core_asset_notes
    label: Asset notes
  - field_name: f_core_country_iso
    label: Country ISO
    values:
      - ABW
      - AFG
      - AGO
      - AIA
      - ALB
      - AND
      - ARE
      - ARG
      - ARM
      - ASM
      - ATG
      - AUS
      - AUT
      - AZE
      - BDI
      - BEL
      - BEN
      - BFA
      - BGD
      - BGR
      - BHR
      - BHS
      - BIH
      - BLM
      - BLR
      - BLZ
      - BMU
      - BOL
      - BRA
      - BRB
      - BRN
      - BTN
      - BWA
      - CAF
      - CAN
      - CHE
      - CHL
      - CHN
      - CIV
      - CMR
      - COD
      - COG
      - COK
      - COL
      - COM
      - CPV
      - CRI
      - CUB
      - CUW
      - CYM
      - CYP
      - CZE
      - DEU
      - DJI
      - DMA
      - DNK
      - DOM
      - DZA
      - ECU
      - EGY
      - ERI
      - ESP
      - EST
      - ETH
      - FIN
      - FJI
      - FLK
      - FRA
      - FRO
      - FSM
      - GAB
      - GBR
      - GEO
      - GGY
      - GHA
      - GIB
      - GIN
      - GMB
      - GNB
      - GNQ
      - GRC
      - GRD
      - GRL
      - GTM
      - GUM
      - GUY
      - HKG
      - HMD
      - HND
      - HRV
      - HTI
      - HUN
      - IDN
      - IMN
      - IND
      - IRL
      - IRN
      - IRQ
      - ISL
      - ISR
      - ITA
      - JAM
      - JEY
      - JOR
      - JPN
      - KAZ
      - KEN
      - KGZ
      - KHM
      - KIR
      - KNA
      - KOR
      - KWT
      - LAO
      - LBN
      - LBR
      - LBY
      - LCA
      - LIE
      - LKA
      - LSO
      - LTU
      - LUX
      - LVA
      - MAC
      - MAF
      - MAR
      - MCO
      - MDA
      - MDG
      - MDV
      - MEX
      - MHL
      - MKD
      - MLI
      - MLT
      - MMR
      - MNE
      - MNG
      - MNP
      - MOZ
      - MRT
      - MSR
      - MUS
      - MWI
      - MYS
      - NAM
      - NCL
      - NER
      - NFK
      - NGA
      - NIC
      - NIU
      - NLD
      - NOR
      - NPL
      - NRU
      - NZL
      - OMN
      - PAK
      - PAN
      - PCN
      - PER
      - PHL
      - PLW
      - PNG
      - POL
      - PRI
      - PRK
      - PRT
      - PRY
      - PSE
      - PYF
      - QAT
      - ROU
      - RUS
      - RWA
      - SAU
      - SDN
      - SEN
      - SGP
      - SGS
      - SHN
      - SLB
      - SLE
      - SLV
      - SMR
      - SOM
      - SPM
      - SRB
      - SSD
      - STP
      - SUR
      - SVK
      - SVN
      - SWE
      - SWZ
      - SXM
      - SYC
      - SYR
      - TCA
      - TCD
      - TGO
      - THA
      - TJK
      - TKM
      - TLS
      - TON
      - TTO
      - TUN
      - TUR
      - TUV
      - TZA
      - UGA
      - UKR
      - URY
      - USA
      - UZB
      - VAT
      - VCT
      - VEN
      - VGB
      - VIR
      - VNM
      - VUT
      - WLF
      - WSM
      - XXK
      - YEM
      - ZAF
      - ZMB
      - ZWE
  - field_name: f_core_applicability_notes
    label: Applicability notes
  - field_name: f_core_scale_applicability
    label: Scale applicability
  - field_name: f_core_function_type
    label: Function type
  - field_name: f_core_approach
    label: Approach
  - field_name: f_core_f_relationship
    label: F relationship
  - field_name: f_core_f_math
    label: Math
  - field_name: f_core_f_math_model
    label: Math model
  - field_name: f_core_bespoke_model_ref
    label: Bespoke model reference
  - field_name: f_core_f_reference
    label: Reference

  ## FSpecifics
  - field_name: fspecifics_par_names
    label: Par names
  - field_name: fspecifics_ub_par_value
    label: UB par value
  - field_name: fspecifics_ub_par_perc
    label: UB par perc
  - field_name: fspecifics_med_par_value
    label: Med par value
  - field_name: fspecifics_lb_par_value
    label: LB par value
  - field_name: fspecifics_lb_par_perc
    label: LB par perc
  - field_name: fspecifics_damage_scale_code
    label: Damage scale code
  - field_name: fspecifics_dm_state_name
    label: DM state name
  - field_name: fspecifics_n_dm_states
    label: N DM states
  - field_name: fspecifics_f_disc_im
    label: F disc IM
  - field_name: fspecifics_f_disc_ep
    label: F disc EP
  - field_name: fspecifics_lp_code
    label: LP code
  - field_name: fspecifics_lp_loss_value
    label: LP loss value
  - field_name: fspecifics_edp_cpde
    label: EDP cpde
  - field_name: fspecifics_edp_name
    label: EDP name
  - field_name: fspecifics_edp_dmstate_thre
    label: EDP dmstate threshold
  - field_name: fspecifics_im_code
    label: IM code
  - field_name: fspecifics_im_name
    label: IM name
  - field_name: fspecifics_im_range
    label: IM range
  - field_name: fspecifics_im_units
    label: IM units
  - field_name: fspecifics_im_method
    label: IM method
  - field_name: fspecifics_im_sim_type
    label: IM sim type
  - field_name: fspecifics_impe_reference
    label: IMPE reference
  - field_name: fspecifics_data_countries
    label: Data countries
  - field_name: fspecifics_im_data_source
    label: IM data source
  - field_name: fspecifics_n_events
    label: N events
  - field_name: fspecifics_n_assets
    label: N assets

  ## FAdditional
  - field_name: fAdditional_nonsampling_err
    label: Nonsampling error
  - field_name: fAdditional_type_nonsampling_err
    label: Type nonsampling err
  - field_name: fAdditional_is_fix_nonsam_err
    label: Is fix nonsam err
  - field_name: fAdditional_is_data_aggregated
    label: Is data aggregated
  - field_name: fAdditional_n_data_points_aggr
    label: N data points aggregated
  - field_name: fAdditional_is_data_disaggr
    label: Is data disaggrated
  - field_name: fAdditional_an_analysis_type
    label: AN analysis type
  - field_name: fAdditional_em_analysis_type
    label: EM analysis type
  - field_name: fAdditional_jd_analysis_type
    label: JD analysis type
  - field_name: fAdditional_is_fit_good
    label: Is fit good
  - field_name: fAdditional_fit_ref
    label: Fit reference
  - field_name: fAdditional_val_data_source
    label: Value data source
  - field_name: fAdditional_val_study_reference
    label: Value study reference
  - field_name: fAdditional_sample
    label: Sample

  ## FScoring
  - field_name: fscoring_geo_applicability
    label: Geo applicability
  - field_name: fscoring_core_id
    label: Core id
  - field_name: fscoring_geographic_relevance_score
    label: Geographic relevance score

  ## DMScale
  - field_name: dmscale_asset_type
    label: Asset type
  - field_name: dmscale_occupancy
    label: Occupancy
  - field_name: dmscale_hazard_type
    label: Hazard type
  - field_name: dmscale_process_type
    label: Process type
  - field_name: dmscale_asset_notes
    label: Asset notes
  - field_name: dmscale_taxonomy_source
    label: Taxonomy source
  - field_name: dmscale_taxonomy
    label: Taxonomy
  - field_name: dmscale_n_dm_states
    label: N DM states
  - field_name: dmscale_dm_states_id
    label: DM states id
  - field_name: dmscale_dm_states_name
    label: DM states name
  - field_name: dmscale_damage_scale_name
    label: Damage scale name
  - field_name: dmscale_damage_scale_code
    label: Damage scale code
  - field_name: dmscale_damage_scale_type
    label: Damage scale type
  - field_name: dmscale_dm_scale_reference
    label: DM scale reference
  - field_name: dmscale_is_edp_thre
    label: Is EDP threshold
  - field_name: dmscale_is_dm_factor
    label: Is DM factor
  - field_name: dmscale_is_casualties
    label: Is casualties
  - field_name: dmscale_is_downtime
    label: Is downtime

  ## EDPTable
  - field_name: edp_code
    label: Code
  - field_name: edp_description
    label: Description
  - field_name: edp_units
    label: Units
  - field_name: edp_name
    label: Name

  ## LPTable
  - field_name: lp_code
    label: Code
  - field_name: lp_name
    label: Name
  - field_name: lp_description
    label: Description
  - field_name: lp_units
    label: Units

  ## ReferenceTable
  - field_name: reftable_author_year
    label: Author year
  - field_name: reftable_title
    label: Title
  - field_name: reftable_issn  # International Standard Serial Number associated with reference
    label: ISSN  # International Standard Serial Number associated with reference
  - field_name: reftable_doi  # Digital Object Identifier url associated with reference
    label: DOI  # Digital Object Identifier url associated with reference

---