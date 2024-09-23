/**
 * Generated by the protoc-gen-ts.  DO NOT EDIT!
 * compiler version: 5.28.2
 * source: forwarder/entity.proto
 * git: https://github.com/thesayyn/protoc-gen-ts */
import * as pb_1 from "google-protobuf";
export class StockNumArr extends pb_1.Message {
    #one_of_decls: number[][] = [];
    constructor(data?: any[] | {
        stock_num_arr?: string[];
        odd?: boolean;
    }) {
        super();
        pb_1.Message.initialize(this, Array.isArray(data) ? data : [], 0, -1, [1], this.#one_of_decls);
        if (!Array.isArray(data) && typeof data == "object") {
            if ("stock_num_arr" in data && data.stock_num_arr != undefined) {
                this.stock_num_arr = data.stock_num_arr;
            }
            if ("odd" in data && data.odd != undefined) {
                this.odd = data.odd;
            }
        }
    }
    get stock_num_arr() {
        return pb_1.Message.getFieldWithDefault(this, 1, []) as string[];
    }
    set stock_num_arr(value: string[]) {
        pb_1.Message.setField(this, 1, value);
    }
    get odd() {
        return pb_1.Message.getFieldWithDefault(this, 2, false) as boolean;
    }
    set odd(value: boolean) {
        pb_1.Message.setField(this, 2, value);
    }
    static fromObject(data: {
        stock_num_arr?: string[];
        odd?: boolean;
    }): StockNumArr {
        const message = new StockNumArr({});
        if (data.stock_num_arr != null) {
            message.stock_num_arr = data.stock_num_arr;
        }
        if (data.odd != null) {
            message.odd = data.odd;
        }
        return message;
    }
    toObject() {
        const data: {
            stock_num_arr?: string[];
            odd?: boolean;
        } = {};
        if (this.stock_num_arr != null) {
            data.stock_num_arr = this.stock_num_arr;
        }
        if (this.odd != null) {
            data.odd = this.odd;
        }
        return data;
    }
    serialize(): Uint8Array;
    serialize(w: pb_1.BinaryWriter): void;
    serialize(w?: pb_1.BinaryWriter): Uint8Array | void {
        const writer = w || new pb_1.BinaryWriter();
        if (this.stock_num_arr.length)
            writer.writeRepeatedString(1, this.stock_num_arr);
        if (this.odd != false)
            writer.writeBool(2, this.odd);
        if (!w)
            return writer.getResultBuffer();
    }
    static deserialize(bytes: Uint8Array | pb_1.BinaryReader): StockNumArr {
        const reader = bytes instanceof pb_1.BinaryReader ? bytes : new pb_1.BinaryReader(bytes), message = new StockNumArr();
        while (reader.nextField()) {
            if (reader.isEndGroup())
                break;
            switch (reader.getFieldNumber()) {
                case 1:
                    pb_1.Message.addToRepeatedField(message, 1, reader.readString());
                    break;
                case 2:
                    message.odd = reader.readBool();
                    break;
                default: reader.skipField();
            }
        }
        return message;
    }
    serializeBinary(): Uint8Array {
        return this.serialize();
    }
    static deserializeBinary(bytes: Uint8Array): StockNumArr {
        return StockNumArr.deserialize(bytes);
    }
}
export class FutureCodeArr extends pb_1.Message {
    #one_of_decls: number[][] = [];
    constructor(data?: any[] | {
        future_code_arr?: string[];
    }) {
        super();
        pb_1.Message.initialize(this, Array.isArray(data) ? data : [], 0, -1, [1], this.#one_of_decls);
        if (!Array.isArray(data) && typeof data == "object") {
            if ("future_code_arr" in data && data.future_code_arr != undefined) {
                this.future_code_arr = data.future_code_arr;
            }
        }
    }
    get future_code_arr() {
        return pb_1.Message.getFieldWithDefault(this, 1, []) as string[];
    }
    set future_code_arr(value: string[]) {
        pb_1.Message.setField(this, 1, value);
    }
    static fromObject(data: {
        future_code_arr?: string[];
    }): FutureCodeArr {
        const message = new FutureCodeArr({});
        if (data.future_code_arr != null) {
            message.future_code_arr = data.future_code_arr;
        }
        return message;
    }
    toObject() {
        const data: {
            future_code_arr?: string[];
        } = {};
        if (this.future_code_arr != null) {
            data.future_code_arr = this.future_code_arr;
        }
        return data;
    }
    serialize(): Uint8Array;
    serialize(w: pb_1.BinaryWriter): void;
    serialize(w?: pb_1.BinaryWriter): Uint8Array | void {
        const writer = w || new pb_1.BinaryWriter();
        if (this.future_code_arr.length)
            writer.writeRepeatedString(1, this.future_code_arr);
        if (!w)
            return writer.getResultBuffer();
    }
    static deserialize(bytes: Uint8Array | pb_1.BinaryReader): FutureCodeArr {
        const reader = bytes instanceof pb_1.BinaryReader ? bytes : new pb_1.BinaryReader(bytes), message = new FutureCodeArr();
        while (reader.nextField()) {
            if (reader.isEndGroup())
                break;
            switch (reader.getFieldNumber()) {
                case 1:
                    pb_1.Message.addToRepeatedField(message, 1, reader.readString());
                    break;
                default: reader.skipField();
            }
        }
        return message;
    }
    serializeBinary(): Uint8Array {
        return this.serialize();
    }
    static deserializeBinary(bytes: Uint8Array): FutureCodeArr {
        return FutureCodeArr.deserialize(bytes);
    }
}
export class ErrorMessage extends pb_1.Message {
    #one_of_decls: number[][] = [];
    constructor(data?: any[] | {
        err?: string;
    }) {
        super();
        pb_1.Message.initialize(this, Array.isArray(data) ? data : [], 0, -1, [], this.#one_of_decls);
        if (!Array.isArray(data) && typeof data == "object") {
            if ("err" in data && data.err != undefined) {
                this.err = data.err;
            }
        }
    }
    get err() {
        return pb_1.Message.getFieldWithDefault(this, 1, "") as string;
    }
    set err(value: string) {
        pb_1.Message.setField(this, 1, value);
    }
    static fromObject(data: {
        err?: string;
    }): ErrorMessage {
        const message = new ErrorMessage({});
        if (data.err != null) {
            message.err = data.err;
        }
        return message;
    }
    toObject() {
        const data: {
            err?: string;
        } = {};
        if (this.err != null) {
            data.err = this.err;
        }
        return data;
    }
    serialize(): Uint8Array;
    serialize(w: pb_1.BinaryWriter): void;
    serialize(w?: pb_1.BinaryWriter): Uint8Array | void {
        const writer = w || new pb_1.BinaryWriter();
        if (this.err.length)
            writer.writeString(1, this.err);
        if (!w)
            return writer.getResultBuffer();
    }
    static deserialize(bytes: Uint8Array | pb_1.BinaryReader): ErrorMessage {
        const reader = bytes instanceof pb_1.BinaryReader ? bytes : new pb_1.BinaryReader(bytes), message = new ErrorMessage();
        while (reader.nextField()) {
            if (reader.isEndGroup())
                break;
            switch (reader.getFieldNumber()) {
                case 1:
                    message.err = reader.readString();
                    break;
                default: reader.skipField();
            }
        }
        return message;
    }
    serializeBinary(): Uint8Array {
        return this.serialize();
    }
    static deserializeBinary(bytes: Uint8Array): ErrorMessage {
        return ErrorMessage.deserialize(bytes);
    }
}
